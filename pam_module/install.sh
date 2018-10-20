gcc -fPIC -fno-stack-protector -c main.c
sudo ld -x --shared -o /lib/security/CVLock.so main.o
