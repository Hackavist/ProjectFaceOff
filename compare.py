import face_recognition
import cv2

img = cv2.imread("Nour.JPG")
resized_image = cv2.resize(img, (600, 600))
resized_imageencoding = face_recognition.face_encodings(resized_image)[0]
print("Still working")

img2 = cv2.imread("Hady.jpg")
unknown_face = cv2.resize(img2, (600, 600))
unknown_face_encoding = face_recognition.face_encodings(unknown_face)[0]

print("Still working")

results = face_recognition.compare_faces([resized_imageencoding], unknown_face_encoding)
print(results)


