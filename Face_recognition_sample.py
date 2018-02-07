import io
import picamera
import cv2
import numpy
from Tkinter import *
import Tkinter as tk
import PIL
import webbrowser
import os
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
from PIL import Image, ImageTk, ImageSequence
from sampleGIF_bb_py2 import App
from CloudWidgets_workingmainpage_py2 import widget_page

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO()

os.system("sudo raspivid -t")
#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters (e.g.:rotate the image)
with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture(stream, format='jpeg')

#Convert the picture into a numpy array
buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

#Now creates an OpenCV image
image = cv2.imdecode(buff, 1)

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

#Convert to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print "Found "+str(len(faces))+" face(s)"

   

#Draw a rectangle around every found face
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

#cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img',image)
#Save the result image
cv2.imwrite('result.jpg',image)
cv2.waitKey(0) & 0xFF

if len(faces)>0:
    root = tk.Tk()
    App = App(root)
    root.configure(background='black')
    root.mainloop()

    we = widget_page()



cv2.waitKey(0)
cv2.destroyAllWindows()
