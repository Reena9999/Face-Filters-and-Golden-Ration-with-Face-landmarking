Both these projects use MediaPipe's face landmarking model.

# Face Filters
This project is an attempt at recreating face filters simalr to Snapchat or Instagram. The MediaPipe model used is Facemesh. 

Workflow:  
--> The camera receives live video feed  
--> The pretrained model is loaded  
--> Frames from the live feed are sent to the pretrained model to identify human faces  
--> if a face is identified:   
    return a list of face landmarks  
--> With the landmarks the image to overlay, here some sun glasses, is resized to fit the human face  
--> Use OpenCV to overlay image on the live feed frame and return the frame.  

# Golden Ration
This is a mathematical formula to calulate the beauty of a face based on the ratio of Phi.  
  
Workflow:  
--> The camera receives live video feed  
--> The pre-trained model is loaded  
--> Upon clicking a the 'Calculate Golden Ration' button a frame is passed to a function.  
--> The function calculates the width, length ratio of the face and returns a number  
--> the closer the number is to the value of phi, the more beautiful the human face is  
  
To read more about golden Ratios read the blog below:  
[url]https://www.goldennumber.net/meisner-beauty-guide-golden-ratio-facial-analysis/  
