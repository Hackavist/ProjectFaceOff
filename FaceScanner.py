import cv2
import face_recognition.api as face_recognition
import PIL.Image
import numpy as np
import logging as log
import datetime as dt
from time import sleep
import os

dir=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(dir,"Images")

for root,dirs,files in os.walk(image_dir):
    for file in files :

        if file.endswith("png")or file.endswith("jpg")or file.endswith("jpeg"):

            path = os.path.join(root, file)
            label=os.path.split(path)[-1]
            label , var = label.split('.')
            img = cv2.imread(path)
            resized_image = cv2.resize(img, (700, 700))
            faces = face_recognition.face_locations(resized_image)
            if len(faces) >= 0:    
                print(len(faces))
                print(path)