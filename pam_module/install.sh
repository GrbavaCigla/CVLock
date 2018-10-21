gcc -fPIC -fno-stack-protector -c main.c
sudo ld -x --shared -o /lib64/security/CVLock.so main.o 2>/dev/null
sudo ld -x --shared -o /lib64/security/CVLock.so main.o 2>/dev/null
