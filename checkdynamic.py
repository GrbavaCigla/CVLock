import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import sys;

mainfolder="/usr/local/CVLock/"
picfolder=join(mainfolder, sys.argv[1])
threshold = 0.7
tickness=2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
files = [join(picfolder,f) for f in listdir(picfolder) if isfile(join(picfolder, f))]

cap = cv2.VideoCapture(0)
while 1:
        for template in files:
                ret, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x,y,w,h) in faces:
                        roi_gray = gray[y:y+h, x:x+w]
                        timg = cv2.imread(template)
                        timg = cv2.cvtColor(timg, cv2.COLOR_BGR2GRAY)
                        res = cv2.matchTemplate(gray,timg,cv2.TM_CCOEFF_NORMED)
                        loc = np.where( res >= threshold)

                        for pt in zip(*loc[::-1]):
                                #LOCK PART
                                print("OK")
                                quit(0)
                                break
                                #LOCK PART	
        if cv2.waitKey(1) & 0xFF == ord('q'):
                quit(54)
cap.release()
cv2.destroyAllWindows()
