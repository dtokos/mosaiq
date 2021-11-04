# -*- coding: utf-8 -*-
from .HSVDeltaCalculator import HSVDeltaCalculator
from .WeightedCalculator import WeightedCalculator

class WeightedHSVDeltaCalculator(HSVDeltaCalculator, WeightedCalculator):
	def calculate(self, pixel, image):
		self._weightPixel(self._toHSV(pixel))
		
		return super(WeightedHSVDeltaCalculator, self).calculate(pixel, image)

	def _hueDelta(self, pixel, image):
		return super(WeightedHSVDeltaCalculator, self)._hueDelta(pixel, image) * self._calculateWeight(pixel, pixel[0])

	def _saturationDelta(self, pixel, image):
		return super(WeightedHSVDeltaCalculator, self)._saturationDelta(pixel, image) * self._calculateWeight(pixel, pixel[1])

	def _valueDelta(self, pixel, image):
		return super(WeightedHSVDeltaCalculator, self)._valueDelta(pixel, image) * self._calculateWeight(pixel, pixel[2])
