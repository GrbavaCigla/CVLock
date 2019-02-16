rm -rf /usr/local/CVLock;
rm -f /lib/security/CVLock.so
mv /etc/pam.d/gdm-fingerprint.old /etc/pam.d/gdm-fingerprint 2> /dev/null
sudo -u gdm gsettings set org.gnome.login-screen enable-fingerprint-authentication false

