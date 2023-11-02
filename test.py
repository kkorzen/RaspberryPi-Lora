from ImageAnalyzer import ImageAnalyzer as IA

path = "picture.jpg"
ia = IA()
ia.PassImage(path)
rgbs = ia.GetAverageRGB()
with open("rgbs.txt", "w") as file:
    for key, val in rgbs.items():
        file.write(f"{key}, {val}\n")
