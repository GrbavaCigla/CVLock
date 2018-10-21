# CVLock
## Description
_CVLock is face recognition authentication for Linux and MacOS Systems. CVLock uses intel's cv2 for recognition._


## Disclaimer
###### **_WE ARE NOT RESPONSIBLE FOR ANY DAMAGE!<br />NO UNICORNS WERE HARMED DURING PROGRAMMING!_**



## Installation
#### Requirement
```
pip3 install opencv-python
pip3 install numpy
```
or
```
sudo apt-get install python3-opencv python3-numpy
```
#### Installing
Then run the installation file with:
```
sudo sh install.sh
```
#### Editing the files

Add following line to `/etc/pam.d/commmon-auth` or `/etc/pam.d/system-auth`:
```
auth sufficient CVLock.so
```
Run `templatemaker.py` without `[]`:
```
sudo python3 templatemaker.py [name]
```
To make sample click `c` on keayboard. Make about 40 samples.
## Credits
Made by [proalexa](https://github.com/proalexa/) and [hwrnr](https://github.com/hwrnr/)<br />
Thanks for cv2 by Intel

