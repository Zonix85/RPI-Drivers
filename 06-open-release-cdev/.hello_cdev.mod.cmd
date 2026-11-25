savedcmd_hello_cdev.mod := printf '%s\n'   hello_cdev.o | awk '!x[$$0]++ { print("./"$$0) }' > hello_cdev.mod
