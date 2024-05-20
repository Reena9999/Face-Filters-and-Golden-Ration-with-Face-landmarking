import streamlit as st
from streamlit_webrtc import webrtc_streamer,RTCConfiguration
import av
import cv2
import mediapipe as mp
import math

def callback(frame):
    img = frame.to_ndarray(format="bgr24")

    img = cv2.cvtColor(frame.to_ndarray(format="bgr24"), cv2.COLOR_BGR2RGB)
    
    mp_face = mp.solutions.face_mesh
    face_mesh = mp_face.FaceMesh()
    result = face_mesh.process(img)
        
    # if result.multi_face_landmarks:

    if calculate_ratio_button:
        keypoints = []
        for landmarks in result.multi_face_landmarks:
            for landmark in landmarks.landmark:
                 keypoints.append({
                         'x': landmark.x,
                         'y': landmark.y,
                         'z': landmark.z,
                         })
                 
        GR=calculate_golden_ratio(img,keypoints)
        print('GR: ',GR)
 
    flipped_frame = cv2.flip(img, 1)
    return av.VideoFrame.from_ndarray(flipped_frame)

def calculate_golden_ratio(img,landmarks):
    golden_ratios=[]
    # RATION BETWEEN Head height AND head width
    head_width=calculate_distance(img,landmarks[234],landmarks[454])
    head_heigth=calculate_distance(img,landmarks[10],landmarks[152])

    # RATIO BETWEEN Facial width AND inner eye to ear
    left_inner_eye_to_ear=calculate_distance(img,landmarks[465],landmarks[454])

    # RATIO BETWEEN Inner eye to outer eye AND outer eye to side of face
    left_eye_distance=calculate_distance(img,landmarks[465],landmarks[359])
    left_outer_eye_to_ear=calculate_distance(img,landmarks[359],landmarks[454])

    # RATION BETWEEN right pupil to center of lip AND center of lip to chin
    # RATION BETWEEN left pupil to center of lip AND center of lip to chin
    right_eye_center={'x':(landmarks[159]['x']+landmarks[145]['x'])/2,'y':(landmarks[159]['y']+landmarks[145]['y'])/2,'z':(landmarks[159]['z']+landmarks[145]['z'])/2}
    left_eye_center={'x':(landmarks[386]['x']+landmarks[374]['x'])/2,'y':(landmarks[386]['y']+landmarks[374]['y'])/2,'z':(landmarks[386]['z']+landmarks[374]['z'])/2}

    left_eye_to_lips=calculate_distance(img,landmarks[14],left_eye_center)
    right_eye_to_lips=calculate_distance(img,landmarks[14],right_eye_center)
    lips_to_chin=calculate_distance(img,landmarks[14],landmarks[152])

    

    # adding the individual golden ratios to an array for ease in calculations
    golden_ratios.append(head_heigth / head_width)
    golden_ratios.append(head_width/left_inner_eye_to_ear)
    golden_ratios.append(left_eye_distance/left_outer_eye_to_ear)
    golden_ratios.append(left_eye_to_lips/lips_to_chin)
    golden_ratios.append(right_eye_to_lips/lips_to_chin)

    golden_ratio=sum(golden_ratios)/len(golden_ratios)
    return golden_ratio
    
def calculate_distance(img,landmark1,landmark2):
    image_height, image_width,_ = img.shape

    # Convert normalized coordinates to pixel coordinates
    x1, y1 = int(landmark1['x'] * image_width), int(landmark1['y'] * image_height)
    x2, y2 = int(landmark2['x'] * image_width), int(landmark2['y'] * image_height)

    # Calculate the Euclidean distance
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def calculate_horizontal_distance(img,landmarks,point1,point2):
    landmark1 = landmarks[point1]
    landmark2 = landmarks[point2]

    image_height, image_width,_ = img.shape

    # Convert normalized coordinates to pixel coordinates
    x1 = int(landmark1['x'] * image_width)
    x2= int(landmark2['x'] * image_width)

    # Calculate the Euclidean distance
    distance = x2 - x1
    return distance


# UI Components
st.title("Golden Ratio")

webrtc_streamer(key="camera", video_frame_callback=callback)

calculate_ratio_button = st.button("Calculate Golden Ration")


