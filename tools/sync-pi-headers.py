"""Refresh the Windows editor's header cache from a Raspberry Pi over SSH."""

import argparse
from pathlib import Path
import subprocess
import tempfile


# The Pi packages the common and generated headers in separate trees.
EXPORT_HEADERS = r"""
set -eu
release=$(uname -r)
test "$(uname -m)" = aarch64 || { echo "Expected an ARM64 Pi kernel" >&2; exit 1; }
build=$(readlink -f "/lib/modules/$release/build")
common=$(sed -n 's|^include \(/.*/\)Makefile$|\1|p' "$build/Makefile")
test -f "$common/include/linux/module.h"
test -f "$build/include/generated/autoconf.h"
stage=$(mktemp -d)
trap 'rm -f "$stage/common" "$stage/build"; rmdir "$stage"' EXIT
ln -s "$common" "$stage/common"
ln -s "$build" "$stage/build"
echo "Copying kernel headers for $release" >&2
tar -C "$stage" -chzf - common/include common/arch/arm64/include \
    build/include/generated build/arch/arm64/include/generated
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pi", help="Pi SSH address, e.g. user@raspberrypi.local")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    cache = root / ".pi-headers"
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        stage = Path(tmp)
        archive = stage / "headers.tar.gz"
        with archive.open("wb") as output:
            subprocess.run(["ssh", "--", args.pi, EXPORT_HEADERS], stdout=output, check=True)
        headers = stage / "headers"
        headers.mkdir()
        subprocess.run(["tar", "-xzf", str(archive), "-C", str(headers)], check=True)
        previous = stage / "previous"
        if cache.exists():
            cache.rename(previous)
        try:
            headers.rename(cache)
        except OSError:
            if previous.exists():
                previous.rename(cache)
            raise
    print(f"VS Code headers ready in {cache}")


if __name__ == "__main__":
    main()
