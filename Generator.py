# -*- coding: utf-8 -*-
import sys
import colorsys

class Generator:
	def __init__(self, images, deltaCalculator, builder, transparencyTreshold = 0.19):
		self._images = images
		self._deltaCalculator = deltaCalculator
		self._builder = builder
		self.transparencyTreshold = transparencyTreshold

	def generate(self, source):
		self._builder.new(source.size)

		for index, pixel in enumerate(source.getdata()):
			pixel = self._normalizePixel(pixel)
			if not self._isTransparent(pixel):
				column = index % source.size[0]
				row = index / source.size[0]
				image = self._findClosestImage(pixel)
				self._builder.paste(image.image, column, row)

		return self._builder.getImage()

	def _isTransparent(self, pixel):
		return pixel[3] < self.transparencyTreshold

	def _normalizePixel(self, pixel):
		return [pixel[0] / 255.0, pixel[1] / 255.0, pixel[2] / 255.0, pixel[3] / 255.0]

	def _findClosestImage(self, pixel):
		closest = None
		delta = sys.maxsize

		for image in self._images:
			imageDelta = self._deltaCalculator.calculate(pixel, image)

			if imageDelta < delta:
				closest = image
				delta = imageDelta

		return closest
