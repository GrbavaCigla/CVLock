mkdir /usr/local/CVLock 2> /dev/null;
cp checkdynamic.py /usr/local/CVLock/;
chmod +x /usr/local/CVLock/checkdynamic.py 
cp haarcascade_frontalface_default.xml /usr/local/CVLock/;
cd pam_module;
./install.sh 2> /dev/null
cd ..;
echo Done installing;
