# -*- coding: utf-8 -*-
from Classifier import Classifier

class AvgRGBClassifier(Classifier):
	def __init__(self, transparencyTreshold = 0.19):
		self.transparencyTreshold = transparencyTreshold

	def classify(self, images):
		return [self.classifyImage(image) for image in images]

	def classifyImage(self, image):
		r = g = b = 0
		numOfPixels = 0
		
		for pixel in image.getdata():
			pixel = self._normalizePixel(pixel)
			if not self._isTransparent(pixel):
				r += pixel[0]
				g += pixel[1]
				b += pixel[2]
				numOfPixels += 1

		if numOfPixels:
			r = r / numOfPixels
			g = g / numOfPixels
			b = b / numOfPixels

		return self.ClassifiedImage(image, r, g, b)

	def _normalizePixel(self, pixel):
		return (pixel[0] / 255.0, pixel[1] / 255.0, pixel[2] / 255.0, pixel[3] / 255.0)

	def _isTransparent(self, pixel):
		return pixel[3] < self.transparencyTreshold
