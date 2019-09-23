# -*- coding: utf-8 -*-
from DeltaCalculator import DeltaCalculator

class HSVDeltaCalculator(DeltaCalculator):
	def calculate(self, pixel, image):
		return float(
			self._hueDelta(pixel, image) +
			self._saturationDelta(pixel, image) +
			self._valueDelta(pixel, image)
		) / 3.0

	def _hueDelta(self, pixel, image):
		return abs(image.h - pixel[0])

	def _saturationDelta(self, pixel, image):
		return abs(image.s - pixel[1])

	def _valueDelta(self, pixel, image):
		return abs(image.v - pixel[2])
