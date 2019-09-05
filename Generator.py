# -*- coding: utf-8 -*-
import colorsys

class Generator:
	class ClassifiedImage:
		def __init__(self, image):
			self.image = image
			self.r = None
			self.g = None
			self.b = None
			self.h = None
			self.s = None
			self.v = None

	TRANSPARENCY_TRESHOLD = 50

	def __init__(self, images, builder):
		self._images = self._clasifyImages(images)
		self._builder = builder

	def _clasifyImages(self, images):
		return [self._classifyImage(image) for image in images]

	def _classifyImage(self, image):
		r = g = b = 0
		numOfPixels = 0
		classifiedImage = self.ClassifiedImage(image)
		
		for pixel in image.getdata():
			if not self._isTransparent(pixel):
				r += pixel[0]
				g += pixel[1]
				b += pixel[2]
				numOfPixels += 1

		r = r / numOfPixels
		g = g / numOfPixels
		b = b / numOfPixels
		h, s, v = self._rgbToHsv(r, g, b)

		classifiedImage.r = r
		classifiedImage.g = g
		classifiedImage.b = b
		classifiedImage.h = h
		classifiedImage.s = s
		classifiedImage.v = v

		return classifiedImage

	def _rgbToHsv(self, r, g, b):
		return colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)

	def _isTransparent(self, pixel):
		return pixel[3] < self.TRANSPARENCY_TRESHOLD

	def generate(self, source):
		self._builder.new(source.size, source.size)

		for index, pixel in enumerate(source.getdata()):
			if not self._isTransparent(pixel):
				column = index % source.size[0]
				row = index / source.size[0]
				image = self._findClosestImage(pixel)
				self._builder.paste(image.image, column, row)

		return self._builder.getImage()

	def _findClosestImage(self, pixel):
		closest = None
		delta = 999

		for image in self._images:
			imageDelta = self._imageDelta(pixel, image)

			if imageDelta < delta:
				closest = image
				delta = imageDelta

		return closest

	def _imageDelta(self, pixel, image):
		return (self._hsvDelta(pixel, image) + self._rgbDelta(pixel, image)) / 2.0

		
	def _hsvDelta(self, pixel, image):
		h, s, v = self._rgbToHsv(pixel[0], pixel[1], pixel[2])
		mh, ms, mv = self._getModifiers(h, s, v)
		idh = abs(image.h - h)
		ids = abs(image.s - s)
		idv = abs(image.v - v)

		return float(idh * mh + ids * ms + idv * mv) / 3.0

	def _rgbDelta(self, pixel, image):
		mr, mg, mb = self._getModifiers(pixel[0], pixel[1], pixel[2])
		idr = abs(image.r - pixel[0])
		idg = abs(image.g - pixel[1])
		idb = abs(image.b - pixel[2])

		return float(idr * mr + idg * mg + idb * mb) / 3.0

	def _getModifiers(self, a, b, c):
		a = float(a)
		b = float(b)
		c = float(c)
		
		modif = [10.0, 10.0, 10.0]
		pixel = [a, b, c]
		maxValue = max(a, b, c)
		minValue = min(a, b, c)
		midValue = [value for value in pixel if value != maxValue and value != minValue]
		midValue = midValue[0] if len(midValue) else (minValue + maxValue) / 2

		for index, value in enumerate(pixel):
			if value == maxValue:
				modif[index] -= (maxValue - midValue) / maxValue * 10.0
			if value == minValue:
				modif[index] += (midValue - minValue) / midValue * 10.0

		return modif

