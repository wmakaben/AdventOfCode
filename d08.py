file = open("input/d08.txt", 'r')

image = file.readline()

width = 25
height = 6

def getMinZeroLayer(image, w, h):
	layer = -1
	layers = {}
	minLayer = None
	i = 0

	while i < len(image):
		skip = False
		if i % (w * h) == 0:
			if layer in layers:
				minLayer = layer
			layer += 1
			layers[layer] = {0: 0, 1: 0, 2: 0}

		# print(i)
		# print(layer, layers[layer])
		if image[i] == '0':
			layers[layer][0] += 1
			if minLayer != None and layers[layer][0] > layers[minLayer][0]:
				del layers[layer]
				skip = True
		elif image[i] == '1':
			layers[layer][1] += 1
		elif image[i] == '2':
			layers[layer][2] += 1

		if skip:
			i = layer * w * h
		else:
			i += 1
	return layers[minLayer]

minLayer = getMinZeroLayer(image, width, height)
print(minLayer, minLayer[1] * minLayer[2])