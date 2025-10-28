from importlib import import_module
from tracemalloc import take_snapshot
import cv2
import dropbox
import time 
import random

start_time = time.time()

def take_snapshots():
    number = random.randint(0, 50)

    ImageCaptureObject = cv2.imageCapture(0)
    result = True
    
    while(result):
        #read frames while camera is on
        ret,frame = ImageCaptureObject.read()

        #cv2.imwrite for saving the images in the cloud storage
        image_name = "img" + str(number) + ".png"

        cv2.imwrite(image_name, frame)

        start_time = time.time()
        result = False

        return image_name

    print("Image Captured!")

    #release the camera
    ImageCaptureObject.release()

    #close all the windows
    cv2.destroyAllWindows()

def upload_files(image_name):
    access_token = "sl.BDup-qZq2GD16uABSi7e3TMhDUKpPUYGhPOCEIUzFsX1PLIPOvnNWzwVAJbUjhU6C5V9TfEvj-Xss5EV9sx7-guGHXh4QBtfBa9grKJDUupF6TaaRpe0LlFxNpGxyAHw8JJZcxce-D_V"
    file = image_name
    file_from = file
    file_to = "/Image_Folder/" + (image_name)

    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 300):
            name = take_snapshots()
            upload_files(name)

main()




