# -*- coding: utf-8 -*-
from RGBDeltaCalculator import RGBDeltaCalculator
from WeightedCalculator import WeightedCalculator

class WeightedRGBDeltaCalculator(RGBDeltaCalculator, WeightedCalculator):
	def calculate(self, pixel, image):
		self._weightPixel(pixel)
		
		return super(WeightedRGBDeltaCalculator, self).calculate(pixel, image)

	def _redDelta(self, pixel, image):
		return super(WeightedRGBDeltaCalculator, self)._redDelta(pixel, image) * self._calculateWeight(pixel, pixel[0])

	def _greenDelta(self, pixel, image):
		return super(WeightedRGBDeltaCalculator, self)._greenDelta(pixel, image) * self._calculateWeight(pixel, pixel[1])

	def _blueDelta(self, pixel, image):
		return super(WeightedRGBDeltaCalculator, self)._blueDelta(pixel, image) * self._calculateWeight(pixel, pixel[2])
