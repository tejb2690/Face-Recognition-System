import cv2
import numpy as np
import sys
import os
from datetime import datetime 
print("Do you want to take test image [y,n ]-->")
option=sys.stdin.readline()
#print("Enter Your Id-->")
#id=int(sys.stdin.readline())
if(option=='n') :
	cv2.destroyAllWindows()	
cap=cv2.VideoCapture(0)
sampleNum=0
#folderName="test_data"
#os.makedirs(folderName)
while 1:
	cv2.waitKey(1000)
	ret,img=cap.read()
	sampleNum +=1
	t=datetime.now().time()
	d=datetime.now().date()
	faceFileName="D:/testProject/final_project/test_data/"+str(d)+"__"+str(t)+".jpg"
	cv2.imwrite(faceFileName,img)
	#yycv2.imshow('face',img)
	cv2.waitKey(1000)
	if(sampleNum>0):
		break
cap.release()
cv2.destroyAllWindows()
	
	
