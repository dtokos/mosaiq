# -*- coding: utf-8 -*-
from PIL import Image

class Builder:
	def __init__(self, tileSize, fillColor = '#00000000'):
		self.fillColor = fillColor
		self._image = None
		self._tileSize = tileSize
		self._resizeCache = None

	def new(self, gridSize):
		self._image = Image.new('RGBA', self._calculateImageSize(gridSize), self.fillColor)
		self._resizeCache = {}

	def paste(self, image, row, column):
		if self._tileSize != image.size:
			image = self._resizeTile(image)
		
		self._image.paste(image, (row * self._tileSize[0], column * self._tileSize[1]), image)

	def getImage(self):
		return self._image

	def _calculateImageSize(self, gridSize):
		return (gridSize[0] * self._tileSize[0], gridSize[1] * self._tileSize[1])

	def _resizeTile(self, image):
		if not image in self._resizeCache:
			self._resizeCache[image] = image.resize(self._tileSize)

		return self._resizeCache[image]
