from picamera2 import Picamera2, Preview
import time

def TakeAShot():
	picam = Picamera2()
	config = picam.create_preview_configuration(main={"size":(1600,1200)})
	picam.configure(config)
	picam.start()
	picam.capture_file("RPi-camphoto.jpg")
	picam.close()
