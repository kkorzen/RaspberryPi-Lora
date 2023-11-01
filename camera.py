from picamera2 import Picamera2, Preview
import time,libcamera

def TakeAShot():
	picam = Picamera2()

	config = picam.create_preview_configuration(main={"size":(1600,1200)})
	# config["transform"] = libcamera.Transform(hflip=1,vflip=1)
	picam.configure(config)

	picam.start()

	picam.capture_file("camphoto.jpg")

	picam.close()
