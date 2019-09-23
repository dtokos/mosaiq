# -*- coding: utf-8 -*-
from DeltaCalculator import DeltaCalculator

class RGBDeltaCalculator(DeltaCalculator):
	def calculate(self, pixel, image):
		return float(
			self._redDelta(pixel, image) +
			self._greenDelta(pixel, image) +
			self._blueDelta(pixel, image)
		) / 3.0

	def _redDelta(self, pixel, image):
		return abs(image.r - pixel[0])

	def _greenDelta(self, pixel, image):
		return abs(image.g - pixel[1])

	def _blueDelta(self, pixel, image):
		return abs(image.b - pixel[2])
