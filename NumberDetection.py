import face_recognition
import cv2


resized_image = cv2.resize(img, (750, 750)) 
face_locations = face_recognition.face_locations(resized_image) 
print(len(face_locations))