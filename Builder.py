# -*- coding: utf-8 -*-
from PIL import Image

class Builder:
	def __init__(self):
		self._image = None
		self._tileSize = None

	def new(self, size, tileSize):
		self._image = Image.new('RGBA', (size[0] * tileSize[0], size[1] * tileSize[1]))
		self._tileSize = tileSize

	def paste(self, image, row, column):
		self._image.paste(image, (row * self._tileSize[0], column * self._tileSize[1]))

	def getImage(self):
		return self._image