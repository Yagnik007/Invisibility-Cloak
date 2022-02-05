#opencv for image processing
import cv2 
#creating a videocapture object
#this is my webcam
#Use cv2.VideoCapture() to get a video capture object for the camera.
#Starting camera. Here, in VideoCapture()-0 denotes built-in webcam while 1 will denote the use of external webcams.
cap = cv2.VideoCapture(1) 
#getting the background image
# In a real-time video monitoring system, to ensure that the camera is opened and working properly we have isOpened() of OpenCV. 
while cap.isOpened():
#simply reading from the web cam
#This code initiates an infinite loop (to be broken later by a break statement), where we have ret and frame being defined as the cap. read(). Basically, ret is a boolean regarding whether or not there was a return at all, at the frame is each frame that is returned.
    ret, background = cap.read() 
    if ret:
        cv2.imshow("image", background)
#Python ord() function returns the Unicode code from a given character. This function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed argument. In other words, given a string of length 1, the ord() function returns an integer representing the Unicode code point of the character when an argument is a Unicode object, or the value of the byte when the argument is an 8-bit string.
        if cv2.waitKey(5) == ord('q'):
            #save the background image
            cv2.imwrite("image.jpg", background)
            break
cap.release()
cv2.destroyAllWindows()
