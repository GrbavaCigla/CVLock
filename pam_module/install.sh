gcc -fPIC -fno-stack-protector -c main.c
ld -x --shared -o /lib/security/pam_CVLock.so main.o 2>/dev/null
ld -x --shared -o /lib64/security/pam_CVLock.so main.o 2>/dev/null
ld -x --shared -o /lib/x86_64-linux-gnu/security/pam_CVLock.so main.o 2>/dev/null
echo 'ps aux | grep checkdynamic.py | awk '{print $2}' | xargs kill; exit 0' >> /etc/gdm/PostLogin/Default 2> /dev/null
chmod +x /etc/gdm/PostLogin/Default 2> /dev/null
echo 'ps aux | grep checkdynamic.py | awk '{print $2}' | xargs kill; exit 0' >> /etc/gdm3/PostLogin/Default 2> /dev/null
chmod +x /etc/gdm3/PostLogin/Default 2> /dev/null
