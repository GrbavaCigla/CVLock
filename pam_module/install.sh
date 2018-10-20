gcc -fPIC -fno-stack-protector -c main.c
sudo ld -x --shared -o /lib/security/mypam.so main.o
