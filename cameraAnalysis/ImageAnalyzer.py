from PIL import Image

ERROR_VAL = -1


class ImageAnalyzer():
    def __init__(self) -> None:
        self.image: Image = None
        self.path = ""
        pass

    def PassImage(self, _path):
        try:
            self.path = _path
            self.image = Image.open(self.path)
        except FileNotFoundError:
            print("ERROR - PassImage(): No such file found. Please check the file path.")

    def GetSize(self):
        try:
            width = self.image.size[0]
            height = self.image.size[1]
            return (width, height)
        except AttributeError:
            print(
                f"ERROR - GetSize(): Cannot get size of an object with type {type(self.image)}")
            return (ERROR_VAL, ERROR_VAL)

    def GetPath(self):
        return (f"Image path: {self.path}")

    def GetAverageRGB(self):
        width, height = self.GetSize()

        if width == ERROR_VAL:
            return ("ERROR - GetAverageRGB(): Cannot get size of an image. Please chcek the file path.")

        rgb_dict = {"R": 0, "G": 0, "B": 0}
        total_size = width * height

        for i in range(width):
            for j in range(height):
                r, g, b = self.image.getpixel((i, j))
                rgb_dict["R"] += r
                rgb_dict["G"] += g
                rgb_dict["B"] += b

        return {color: round(val/total_size) for color, val in rgb_dict.items()}
