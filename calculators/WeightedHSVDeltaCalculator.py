# -*- coding: utf-8 -*-
from HSVDeltaCalculator import HSVDeltaCalculator

class WeightedHSVDeltaCalculator(HSVDeltaCalculator):
	def __init__(self, hW = 10.0, sW = 10.0, vW = 10.0):
		self.hWeight = hW;
		self.sWeight = sW;
		self.vWeight = vW;

	def _hueDelta(self, pixel, image):
		return super(WeightedHSVDeltaCalculator, self)._hueDelta(pixel, image) * self._hueWeight(pixel);

	def _hueWeight(self, pixel):
		return self._calculateWeights(pixel)[0];

	def _saturationDelta(self, pixel, image):
		return super(WeightedHSVDeltaCalculator, self)._saturationDelta(pixel, image) * self._saturationWeight(pixel);

	def _saturationWeight(self, pixel):
		return self._calculateWeights(pixel)[1];

	def _valueDelta(self, pixel, image):
		return super(WeightedHSVDeltaCalculator, self)._valueDelta(pixel, image) * self._valueWeight(pixel);

	def _valueWeight(self, pixel):
		return self._calculateWeights(pixel)[2];

	def _calculateWeights(self, pixel):
		hsvPixel = pixel[:-1]
		weigths = [self.hWeight, self.sWeight, self.vWeight]
		maxValue = max(hsvPixel)
		minValue = min(hsvPixel)
		midValue = [value for value in hsvPixel if value != maxValue and value != minValue]
		midValue = midValue[0] if len(midValue) else (minValue + maxValue) / 2

		for index, value in enumerate(hsvPixel):
			if value == maxValue:
				weigths[index] -= (maxValue - midValue) / maxValue * 10.0
			if value == minValue:
				weigths[index] += (midValue - minValue) / midValue * 10.0
		
		return weigths
