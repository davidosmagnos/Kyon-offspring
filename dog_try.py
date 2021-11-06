import cv2, dlib, os
import numpy as np
from imutils import face_utils
from numpy.lib import index_tricks, shape_base
from urllib.parse import quote
import base64



def extract_index_array(nparray):
    index = None
    for num in nparray[0]:
        index = num
        break
    return index
def resize(img1):
    w = int(img1.shape[1]*50/100)
    h = int(img1.shape[0]*50/100)
    size = (300,300)
    img1 = cv2.resize(img1,size)
    return img1


def faceSwap(filepath1: str, filepath2: str):
    #reading images
    img1 =cv2.imread(filepath1)
    img_gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)



    # img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    # img1 = cv2.resize(img1, dsize=None, fx=0.5, fy=0.5)
    img2 = cv2.imread(filepath2)
    img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    img_new_face = np.zeros_like(img2)

    # img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    # img2 = cv2.resize(img2, dsize=None, fx=0.5, fy=0.5)



    #masks
    mask = np.zeros_like(img_gray1)

    detector = dlib.cnn_face_detection_model_v1('dogHeadDetector.dat')

    #redictor = dlib.shape_predictor("landmarkDetector.dat")

    predictor = dlib.shape_predictor("predictor_30v2.dat")#test


    # excluded_points = list(range(27,31)) + list(range(31,34)) + list(range(48,68))
    # excluded_points.append(35)




    shapes = []

    #face 1 
    detection_1 = detector(img1, upsample_num_times=1)
    img_result = img1.copy()
    for i, d in enumerate(detection_1):
        coordinates = predictor(img1, d.rect)
        # shape = face_utils.shape_to_np(shape) -- converts "shapes" to nparray

        landmarks_points = []
        #print("number of shapes",len(shape))
        for n in range(0,18):

            x= coordinates.part(n).x #x coordinate of point
            y = coordinates.part(n).y #y coordinate of point

            
            landmarks_points.append((x,y))

            #shapes.append(shape)

            #creates landmarks and with labels
            cv2.circle(img_result, (x,y), radius=3, color = (0,0,255), thickness=-1, lineType=cv2.LINE_AA)
            cv2.putText(img_result, str(n), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
            

        points = np.array(landmarks_points, np.int32)
        convexHull = cv2.convexHull(points)

        #getting a mask background
        cv2.fillConvexPoly(mask, convexHull, 255 )
        #extracted face added to the mask
        dog_face_1 = cv2.bitwise_and(img1, img1, mask= mask)

        # Getting Triangles 
        rect = cv2.boundingRect(convexHull)
        # (x, y, w, h) = rect
        # cv2.rectangle(img_result, (x,y), (x + w, y + h), (0, 255, 0) )

        subdiv = cv2.Subdiv2D(rect)
        subdiv.insert(landmarks_points)
        
        triangles = subdiv.getTriangleList()
        triangles = np.array(triangles, dtype=np.int32)#convert points to int


        indexes_triangles= []

        #print("Triangle", t) All the x and y points get
        for t in triangles:
            pt1 = (t[0],t[1])#points of x and y of point 1
            pt2 = (t[2],t[3])
            pt3 = (t[4],t[5])

            index_pt1 = np.where((points == pt1).all(axis=1))
            
            index_pt1 = extract_index_array(index_pt1)

            index_pt2 = np.where((points == pt2).all(axis=1))
            index_pt2 = extract_index_array(index_pt2)

            index_pt3 = np.where((points == pt3).all(axis=1))
            index_pt3 = extract_index_array(index_pt3)

            #print(index_pt1, index_pt2, index_pt3)

            if index_pt1 is not None and index_pt2 is not None and index_pt3 is not None:
                triangle = [index_pt1, index_pt2, index_pt3]
                indexes_triangles.append(triangle)
        
            #connect each points with a line
            # cv2.line(img1, pt1, pt2, (0, 0, 255), 2)
            # cv2.line(img1, pt2, pt3, (0, 0, 255), 2)
            # cv2.line(img1, pt1, pt3, (0, 0, 255), 2)

    #face of image 2
    detection_2 = detector(img2, upsample_num_times = 1)

    img_result2 = img2.copy()
    for i, d in enumerate(detection_2):
        coordinates = predictor(img2, d.rect)#this produces the x and y values
        landmarks_points2 = []

        for n in range(0,18):
            x = coordinates.part(n).x
            y = coordinates.part(n).y

            
            landmarks_points2.append((x,y))#appends the x and y values

            points2 = np.array(landmarks_points2, np.int32)
            convexhull2 = cv2.convexHull(points2)

            #creates landmarks and with labels
            cv2.circle(img_result2, (x,y), radius=3, color = (0,0,255), thickness=-1, lineType=cv2.LINE_AA)
            cv2.putText(img_result2, str(n), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)

            #cv2.circle(img2, (x, y), 3, (0, 255, 0), -1)
    lines_space_mask = np.zeros_like(img_gray1)
    lines_space_new_face = np.zeros_like(img2)



    # Delaunay Triangulation of both faces
    for triangle_index in indexes_triangles:

    # Triangulation of First Face
        tr1_pt1 = landmarks_points[triangle_index[0]]
        tr1_pt2 = landmarks_points[triangle_index[1]]
        tr1_pt3 = landmarks_points[triangle_index[2]]
        triangle1 = np.array([tr1_pt1, tr1_pt2, tr1_pt3], np.int32)

        rect1 = cv2.boundingRect(triangle1)
        (x, y, w, h) = rect1
        cropped_triangle = img1[y: y + h, x: x+w]
        cropped_tr1_mask = np.zeros((h, w), np.uint8)

        points = np.array([[tr1_pt1[0] -x , tr1_pt1[1] -y],[tr1_pt2[0] -x , tr1_pt2[1] -y],[tr1_pt3[0] -x, tr1_pt3[1] - y ]], np.int32)
        
        cv2.fillConvexPoly(cropped_tr1_mask, points, 255 )
        #cropped_triangle = cv2.bitwise_and(cropped_triangle, cropped_triangle, mask=cropped_tr1_mask)

        # Connecting each points with line
        # cv2.line(img_result, tr1_pt1, tr1_pt2, (0, 0, 255), 2)
        # cv2.line(img_result, tr1_pt3, tr1_pt2, (0, 0, 255), 2)
        # cv2.line(img_result, tr1_pt1, tr1_pt3, (0, 0, 255), 2)

        #Lines Space
        cv2.line(lines_space_mask, tr1_pt1, tr1_pt2, 255)
        cv2.line(lines_space_mask, tr1_pt2, tr1_pt3, 255)
        cv2.line(lines_space_mask, tr1_pt1, tr1_pt3, 255)
        line_space = cv2.bitwise_and(img1, img1, mask= lines_space_mask)

    # Triangulation of the second face
        tr2_pt1 = landmarks_points2[triangle_index[0]]
        tr2_pt2 = landmarks_points2[triangle_index[1]]
        tr2_pt3 = landmarks_points2[triangle_index[2]]
        triangle2 = np.array([tr2_pt1, tr2_pt2, tr2_pt3], np.int32)

        rect2 = cv2.boundingRect(triangle2)
        (x, y, w, h) = rect2

        #creating mask
        cropped_tr2_mask = np.zeros((h, w), np.uint8)

        points2 = np.array([[tr2_pt1[0] -x , tr2_pt1[1] -y],[tr2_pt2[0] -x , tr2_pt2[1] -y],[tr2_pt3[0] -x, tr2_pt3[1] - y ]], np.int32)
        cv2.fillConvexPoly(cropped_tr2_mask, points2, 255 )

        # Connecting each points with line
        # cv2.line(img_result2, tr2_pt1, tr2_pt2, (0, 0, 255), 2)
        # cv2.line(img_result2, tr2_pt3, tr2_pt2, (0, 0, 255), 2)
        # cv2.line(img_result2, tr2_pt1, tr2_pt3, (0, 0, 255), 2)


    # Warping of Triangles
        points = np.float32(points)
        points2 = np.float32(points2)
        M = cv2.getAffineTransform(points, points2)
        warp_triangle =  cv2.warpAffine(cropped_triangle, M, (w, h))
        warp_triangle = cv2.bitwise_and(warp_triangle, warp_triangle, mask=cropped_tr2_mask)
        
        # Reconstruct destination face
        triangle_area = img_new_face[y: y + h, x: x + w]
        triangle_area_gray = cv2.cvtColor(triangle_area, cv2.COLOR_BGR2GRAY)
        _, mask_triangles_designed = cv2.threshold(triangle_area_gray, 1,255, cv2.THRESH_BINARY_INV)
        warp_triangle = cv2.bitwise_and(warp_triangle, warp_triangle, mask= mask_triangles_designed)

        triangle_area = cv2.add(triangle_area, warp_triangle)
        img_new_face[y: y + h, x: x + w] = triangle_area

        


    img_face_mask = np.zeros_like(img_gray2)
    img_head_mask = cv2.fillConvexPoly(img_face_mask, convexhull2, 255)   
    img_face_mask = cv2.bitwise_not(img_head_mask)

    img_head_noface = cv2.bitwise_and(img2, img2, mask=img_face_mask)
    result = cv2.add(img_head_noface, img_new_face)

    (x, y, w, h) = cv2.boundingRect(convexhull2)
    center_face2 = (int((x + x + w) / 2), int((y + y + h) / 2))

    seamlessclone = cv2.seamlessClone(result, img2, img_head_mask, center_face2, cv2.NORMAL_CLONE)
    

    retval, buffer = cv2.imencode('.jpg', seamlessclone)
    image_as_text = base64.b64encode(buffer)

    return {'image_with_landmarks': 'data:image/png;base64,{}'.format(quote(image_as_text)),"image":seamlessclone}
    #cv2.imwrite("result.png", seamlessclone)

# cv2.imshow("Dog 1", img1)
# cv2.imshow("Dog 2", img2)




# cv2.imshow('Result',seamlessclone)
# cv2.waitKey(0)
# cv2.destroyAllWindows()