gcc -fPIC -fno-stack-protector -c main.c
sudo ld -x --shared -o /lib/security/pam_CVLock.so main.o 2>/dev/null
sudo ld -x --shared -o /lib64/security/pam_CVLock.so main.o 2>/dev/null
sudo ld -x --shared -o /lib/x86_64-linux-gnu/security/pam_CVLock.so main.o 2>/dev/null
