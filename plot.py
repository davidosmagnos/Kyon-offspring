import cv2
import numpy as np
import dlib
img1 = cv2.imread("test5.jpg")
img2 = cv2.imread("dog2.jpg")
img1g = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2g = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

predictor = dlib.shape_predictor("predictor_30v2.dat")
detector = dlib.cnn_face_detection_model_v1('dogHeadDetector.dat')

faces = detector(img1g)

for face,rect in enumerate(faces):
    landmarks = predictor(img1g,rect.rect)
    l_points = []

    for n in range(0,18):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        l_points.append((x,y))

        cv2.circle(img1,(x,y),3,(0,0,255,),-1)


# for face,rect in enumerate(faces):
#     landmarks = predictor(img2g,rect.rect)
#     l_points = []

#     for n in range(0,18):
#         x = landmarks.part(n).x
#         y = landmarks.part(n).y
#         l_points.append((x,y))

#         cv2.circle(img2,(x,y),3,(0,0,255,),-1)



cv2.imshow("Points",img1)
# cv2.imshow("Point",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
