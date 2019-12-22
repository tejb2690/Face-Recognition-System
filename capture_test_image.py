#image processing 
import cv2
# mathematical work
import numpy as np

import sys
import os
#face_cascade=cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
#capture videos from the camera
cap=cv2.VideoCapture(0)

id=sys.stdin.readline()
sampleNum=0
while 1:
	ret,img=cap.read()
	#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#faces=face_cascade.detectMultiScale(gray,1.3,5)
	#faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

	sampleNum +=1
	#roi_gray = gray[y:y+h, x:x+w]
	faceFileName="D:/testProject/final_project/test_data/"+"pic"+str(id)+".jpg"
	cv2.imwrite(faceFileName,img)
	#cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
	cv2.waitKey(100)
	cv2.imshow('face',img)
	cv2.waitKey(100)
	if(sampleNum>0):
		break
cap.release()
cv2.destroyAllWindows()
	
	
