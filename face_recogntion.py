import face_recognition_models
import dlib
from  helper_module import _trim_css_to_bounds,_rect_to_css,_css_to_rect
import numpy as np
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
#defining the allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# getting  the face detector object
face_detector = dlib.get_frontal_face_detector()
#getting the shape predictor object
predictor_68_point_model = face_recognition_models.pose_predictor_model_location()
pose_predictor_68_point = dlib.shape_predictor(predictor_68_point_model)

predictor_5_point_model = face_recognition_models.pose_predictor_five_point_model_location()
pose_predictor_5_point = dlib.shape_predictor(predictor_5_point_model)

#getting the face detector model location
cnn_face_detection_model = face_recognition_models.cnn_face_detector_model_location()


#creating the cnn_face detector object
cnn_face_detector = dlib.cnn_face_detection_model_v1(cnn_face_detection_model)
#print(cnn_face_detector)

face_recognition_model = face_recognition_models.face_recognition_model_location()
face_encoder = dlib.face_recognition_model_v1(face_recognition_model)


def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
    
    return list(face_distance(known_face_encodings, face_encoding_to_check) <= tolerance)

# getting the face encoding from the face


def face_encodings(face_image, known_face_locations=None):
 
    raw_landmarks = _raw_face_landmarks(face_image, known_face_locations, model="large")
    return [np.array(face_encoder.compute_face_descriptor(face_image, raw_landmark_set)) for raw_landmark_set in raw_landmarks]





def _raw_face_landmarks(face_image, face_locations=None, model="large"):
    if face_locations is None:
        face_locations = _raw_face_locations(face_image)
    else:
        face_locations = [_css_to_rect(face_location) for face_location in face_locations]

    pose_predictor = pose_predictor_68_point

    if model == "small":
        pose_predictor = pose_predictor_5_point

    return [pose_predictor(face_image, face_location) for face_location in face_locations]

def face_landmarks(face_image, face_locations=None):
   
    landmarks = _raw_face_landmarks(face_image, face_locations)
    landmarks_as_tuples = [[(p.x, p.y) for p in landmark.parts()] for landmark in landmarks]

    
    return [{
        "chin": points[0:17],
        "left_eyebrow": points[17:22],
        "right_eyebrow": points[22:27],
        "nose_bridge": points[27:31],
        "nose_tip": points[31:36],
        "left_eye": points[36:42],
        "right_eye": points[42:48],
        "top_lip": points[48:55] + [points[64]] + [points[63]] + [points[62]] + [points[61]] + [points[60]],
        "bottom_lip": points[54:60] + [points[48]] + [points[60]] + [points[67]] + [points[66]] + [points[65]] + [points[64]]
    } for points in landmarks_as_tuples]


def _raw_face_locations(img, number_of_times_to_upsample=1, model="hog"):
    
    if model == "cnn":
        return cnn_face_detector(img, number_of_times_to_upsample)
    else:
        return face_detector(img, number_of_times_to_upsample)


def face_locations(img, number_of_times_to_upsample=1, model="hog"):
   
    if model == "cnn":
        return [_trim_css_to_bounds(_rect_to_css(face.rect), img.shape) for face in _raw_face_locations(img, number_of_times_to_upsample, "cnn")]
    else:
        return [_trim_css_to_bounds(_rect_to_css(face), img.shape) for face in _raw_face_locations(img, number_of_times_to_upsample, model)]




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
