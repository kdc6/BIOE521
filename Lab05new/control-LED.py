#! /usr/bin/python
# Team11-HouseofPies
#Melody Tan and Katelin Cherry

import picamera

camera = picamera.PiCamera()
# Turn the camera's LED off
camera.led = False
# Take a picture while the LED remains off
camera.capture('foo.jpg')