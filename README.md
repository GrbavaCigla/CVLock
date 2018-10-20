# CVLock
## Description
_CVLock is face recognition authentication for Linux and MacOS Systems. CVLock uses intel's cv2 for recognition._


## Disclaimer
###### **_WE ARE NOT RESPONSIBLE FOR ANY DAMAGE!<br />NO UNICORNS WERE HARMED DURING PROGRAMMING!_**



## Installation
#### Requirement
```
pip install opencv-python
pip install numpy
```
or
```
sudo apt-get install python3-opencv python3-numpy
```
#### Editing the files
Run install.sh file with:
```
sh install.sh
```
Add following line to `/etc/pam.d/commmon-auth` or `/etc/pam.d/system-auth`:
```
auth sufficient CVLock.so
```
## Credits
Made by [proalexa](https://github.com/proalexa/) and [hwrnr](https://github.com/hwrnr/)<br />
Thanks for cv2 by Intel

