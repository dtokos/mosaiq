# -*- coding: utf-8 -*-
from PIL import Image

class Builder:
	def __init__(self, tileSize):
		self._image = None
		self._tileSize = tileSize

	def new(self, gridSize):
		self._image = Image.new('RGBA', (gridSize[0] * self._tileSize[0], gridSize[1] * self._tileSize[1]))

	def paste(self, image, row, column):
		self._image.paste(image, (row * self._tileSize[0], column * self._tileSize[1]))

	def getImage(self):
		return self._image