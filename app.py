from cameraAnalysis.ImageAnalyzer import ImageAnalyzer as IA
import cameraAnalysis.camera as cam

RPI_PHOTO_PATH = "RPi-camphoto.jpg"

# Using PiCamera to take a picture
# Image is stored as the 'RPi-camphoto.jpg' file
cam.TakeAShot()

# Using ImageAnalyzer class to calculate average rgb of an image
ia = IA()
ia.PassImage(RPI_PHOTO_PATH)
rgbs = ia.GetAverageRGB()

# Write calculated average rgb to the text file 'rgbs.txt'
with open("rgbs.txt", "w", encoding = "UTF-8") as file:
    for key, val in rgbs.items():
        file.write(f"{key}:{val}\n")
