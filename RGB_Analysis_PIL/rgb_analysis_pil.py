from PIL import Image

def get_RGB(_img, _dict):
	width = _img.size[0]
	height = _img.size[1]
	
	img = _img.convert("RGB")
	
	for i in range(width):
		for j in range(height):
			r, g, b = img.getpixel((i,j))
			_dict["red"] += r
			_dict["green"] += g
			_dict["blue"] += b
			
			
def RGB_avg():
	path = "camphoto.jpg"
	img = Image.open(path)
	total_size = img.size[0] * img.size[1]

	rgbs = {
		"red":0,
		"green":0,
		"blue":0
	}

	get_RGB(img, rgbs)

	rgbs_avg = { color : round(val/total_size) for color, val in rgbs.items()}
	
	return rgbs_avg


