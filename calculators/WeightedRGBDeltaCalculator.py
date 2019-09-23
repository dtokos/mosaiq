# -*- coding: utf-8 -*-
from RGBDeltaCalculator import RGBDeltaCalculator

class WeightedRGBDeltaCalculator(RGBDeltaCalculator):
	def __init__(self, weight = 10.0):
		self.weight = weight

	def _redDelta(self, pixel, image):
		return super(WeightedRGBDeltaCalculator, self)._redDelta(pixel, image) * self._calculateWeight(pixel, pixel[0])

	def _greenDelta(self, pixel, image):
		return super(WeightedRGBDeltaCalculator, self)._greenDelta(pixel, image) * self._calculateWeight(pixel, pixel[1])

	def _blueDelta(self, pixel, image):
		return super(WeightedRGBDeltaCalculator, self)._blueDelta(pixel, image) * self._calculateWeight(pixel, pixel[2])

	def _calculateWeight(self, pixel, value):
		rgbPixel = pixel[0:3]
		rgbPixel.sort()

		if value == rgbPixel[0]:
			return self.weight + (rgbPixel[1] - rgbPixel[0]) / rgbPixel[1] * self.weight
		elif value == rgbPixel[2]:
			return self.weight - (rgbPixel[2] - rgbPixel[1]) / rgbPixel[2] * self.weight
		else:
			return self.weight
