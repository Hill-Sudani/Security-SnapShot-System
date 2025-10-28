import cv2
from numpy import take

def take_snapshots():
    #initializing cv2
    ImageCaptureObject = cv2.imageCapture(0)
    result = True
    
    while(result):
        #read frames while camera is on
        ret,frame = ImageCaptureObject.read()
        print(ret)
        
        #cv2.imwrite for saving images to storage device
        cv2.imwrite("NewPicture1.png",frame)
        result = False

        #release the camera
        ImageCaptureObject.release()

        #close all the windows
        cv2.destroyAllWindows()

take_snapshots()
