mkdir /usr/local/CVLock 2> /dev/null;
cp checkdynamic.py /usr/local/CVLock/;
cp haarcascade_frontalface_default.xml /usr/local/CVLock/;
cd pam_module;
./install.sh
cd ..;
echo Done installing;
