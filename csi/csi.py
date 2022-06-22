import re

flags = re.MULTILINE | re.IGNORECASE
pattern = re.compile(r"/((?:\d+)x(?:\d+))\|(\d+)\|(\d+)#(\w+)", flags)

def structure(list):
	data = {
		"pixels": list[0].split("x"),
		"x": list[1],
		"y": list[2],
		"color": list[3]
	}
	return data

def decode(string):
	strings = pattern.findall(string)
	params = []

	for param in strings:
		params.append(structure(param))

	return params


class CSIimage:
	"""CSI Image class"""
	def __init__(self, file, **config):
		"""Initialisation CSI Image"""
		self.image = file
		self.svg = '<svg xmlns="http://www.w3.org/2000/svg" ' + \
		' '.join([f'{k}="{config[k]}"' for k in config]) + ">"

	def save(self, dest):
		for x in decode(self.image.read()):
			self.svg += f'<rect width="{x["pixels"][0]}" height="{x["pixels"][1]}" \
			x="{x["x"]}" y="{x["y"]}" fill="#{x["color"]}"/>'

		self.svg += "</svg>"
		with open(dest, "x") as f:
			f.write(self.svg)