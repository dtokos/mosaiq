# -*- coding: utf-8 -*-
from RGBDeltaCalculator import RGBDeltaCalculator

class WeightedRGBDeltaCalculator(RGBDeltaCalculator):
	def __init__(self, rW = 10.0, gW = 10.0, bW = 10.0):
		self.rWeight = rW;
		self.gWeight = gW;
		self.bWeight = bW;

	def _redDelta(self, pixel, image):
		return super(WeightedRGBDeltaCalculator, self)._redDelta(pixel, image) * self._redWeight(pixel);

	def _redWeight(self, pixel):
		return self._calculateWeights(pixel)[0];

	def _greenDelta(self, pixel, image):
		return super(WeightedRGBDeltaCalculator, self)._greenDelta(pixel, image) * self._greenWeight(pixel);

	def _greenWeight(self, pixel):
		return self._calculateWeights(pixel)[1];

	def _blueDelta(self, pixel, image):
		return super(WeightedRGBDeltaCalculator, self)._blueDelta(pixel, image) * self._blueWeight(pixel);

	def _blueWeight(self, pixel):
		return self._calculateWeights(pixel)[2];

	def _calculateWeights(self, pixel):
		rgbPixel = pixel[:-1]
		weigths = [self.rWeight, self.gWeight, self.bWeight]
		maxValue = max(rgbPixel)
		minValue = min(rgbPixel)
		midValue = [value for value in rgbPixel if value != maxValue and value != minValue]
		midValue = midValue[0] if len(midValue) else (minValue + maxValue) / 2

		for index, value in enumerate(rgbPixel):
			if value == maxValue:
				weigths[index] -= (maxValue - midValue) / maxValue * 10.0
			if value == minValue:
				weigths[index] += (midValue - minValue) / midValue * 10.0

		return weigths
