# -*- coding: utf-8 -*-
from HSVDeltaCalculator import HSVDeltaCalculator

class WeightedHSVDeltaCalculator(HSVDeltaCalculator):
	def __init__(self, weight = 10.0):
		self.weight = weight

	def _hueDelta(self, pixel, image):
		return super(WeightedHSVDeltaCalculator, self)._hueDelta(pixel, image) * self._calculateWeight(pixel, pixel[0])

	def _saturationDelta(self, pixel, image):
		return super(WeightedHSVDeltaCalculator, self)._saturationDelta(pixel, image) * self._calculateWeight(pixel, pixel[1])

	def _valueDelta(self, pixel, image):
		return super(WeightedHSVDeltaCalculator, self)._valueDelta(pixel, image) * self._calculateWeight(pixel, pixel[2])

	def _calculateWeight(self, pixel, value):
		hsvPixel = pixel[0:3]
		hsvPixel.sort()

		if value == hsvPixel[0]:
			return self.weight + (hsvPixel[1] - hsvPixel[0]) / hsvPixel[1] * self.weight
		elif value == hsvPixel[2]:
			return self.weight - (hsvPixel[2] - hsvPixel[1]) / hsvPixel[2] * self.weight
		else:
			return self.weight
