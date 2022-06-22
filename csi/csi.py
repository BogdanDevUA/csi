import re

Flags = re.MULTILINE | re.IGNORECASE
Pattern = re.compile(r"/((?:\d+)x(?:\d+))\|(\d+)\|(\d+)#(\w+)", Flags)

def structure(list):
	return {
		"pixels": list[0].split("x"),
		"x": list[1],
		"y": list[2],
		"color": list[3]
	}

def decode(string):
	strings = Pattern.findall(string)
	params = []

	for param in strings:
		params.append(structure(param))

	return params


class CSIimage:
	def __init__(self, file, **config):
		self.image = file
		self.svg = f'<svg xmlns="http://www.w3.org/2000/svg" ' + ' '.join([f'{k}="{config[k]}"' for k in config]) + ">"

	def save(self, dest):
		for x in decode(self.image.read()):
			self.svg += f'<rect width="{x["pixels"][0]}" height="{x["pixels"][1]}" x="{x["x"]}" y="{x["y"]}" fill="#{x["color"]}"/>'

		self.svg += "</svg>"
		with open(dest, "x") as f:
			f.write(self.svg)