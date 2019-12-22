import PIL.Image

import math

import numpy as np

from sklearn import neighbors

import os

import re

import os.path

import pickle

import dlib

from PIL import Image, ImageDraw

import face_recognition_models


#module for geting four co-ordinate of an image (top, right, bottom , left)
def _rect_to_css(rect):
   
    return rect.top(), rect.right(), rect.bottom(), rect.left()



# returning rectangle from given four co-ordinates
def _css_to_rect(css):
	return dlib.rectangle(css[3],css[0],css[1],css[2])




# to check whether image in bound or not
def _trim_css_to_bounds(css, image_shape):
    
    return max(css[0], 0), min(css[1], image_shape[1]), min(css[2], image_shape[0]), max(css[3], 0)


# calculating face distance
def face_distance(face_encodings, face_to_compare):

    if len(face_encodings) == 0:
        return np.empty((0))

    return np.linalg.norm(face_encodings - face_to_compare, axis=1)



# loading an image in RGB fromat i.e to return an numpy array of three channels 

def load_image_file(file, mode='RGB'):
   
    im = PIL.Image.open(file)
    if mode:
        im = im.convert(mode)
    return np.array(im)




# to extract images from from the folder as well as to check if these images are valid or not
def folder_image(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]



#for comparing faces encodings 
def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
   
    return list(face_distance(known_face_encodings, face_encoding_to_check) <= tolerance)


