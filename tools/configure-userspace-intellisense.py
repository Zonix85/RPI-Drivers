"""Generate per-file IntelliSense settings for the userspace test programs.

Run again after adding a test.c or moving the checkout. Kernel sources retain
the ARM64 kernel configuration in .vscode/c_cpp_properties.json.
The default compiler is the local GCC; Windows GCC provides standard C headers
but does not provide Linux-only APIs such as sys/ioctl.h.
"""

import argparse
import json
from pathlib import Path
import shutil


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compiler", default="gcc", help="GCC executable or path")
    args = parser.parse_args()
    compiler = shutil.which(args.compiler)
    if compiler is None:
        parser.error(f"Compiler not found: {args.compiler}")
    root = Path(__file__).resolve().parents[1]
    entries = [
        {
            "directory": root.as_posix(),
            "file": source.as_posix(),
            "arguments": [
                Path(compiler).as_posix(), "-std=gnu11", "-c", source.as_posix()
            ],
        }
        for source in sorted(root.glob("*/test.c"))
    ]
    output = root / ".vscode" / "compile_commands.json"
    output.write_text(json.dumps(entries, indent=4) + "\n", encoding="utf-8")
    print(f"Configured {len(entries)} userspace files with {compiler}")


if __name__ == "__main__":
    main()
