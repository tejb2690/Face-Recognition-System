import cv2
import numpy as np
import sys
import os

#get the name from the terminal
print("Enter Your Name-->")
name=str(sys.stdin.readline())
#get the id
print("Enter Your Id-->")
id=int(sys.stdin.readline())
# 0 corresponods to system's camera
cap=cv2.VideoCapture(0)
sampleNum=0
#folder's name
folderName="D:/testProject/final_project/training_data/"+name+str(id)

#make folder
os.makedirs(folderName)
while 1: 
        # img contains the image frame and ret contains true or false
	ret,img=cap.read()
	sampleNum +=1
	# image full path with image name

	faceFileName="D:/testProject/final_project/training_data/"+name+str(id)+"/"+str(sampleNum)+".jpg"

	#save the image
  
	cv2.imwrite(faceFileName,img)
	#show the image to the user

	cv2.imshow('face',img)
	cv2.waitKey(1000)
	if(sampleNum>4):
		break
#release the cap
cap.release()
#destroy all open windows
cv2.destroyAllWindows()
	
	
