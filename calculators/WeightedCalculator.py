# -*- coding: utf-8 -*-
from .DeltaCalculator import DeltaCalculator

class WeightedCalculator(DeltaCalculator):
	def __init__(self, weight = 10.0):
		self.weight = weight
		self._weightedPixel = None

	def _weightPixel(self, pixel):
		self._weightedPixel = pixel[0:3]
		self._weightedPixel.sort()

	def _calculateWeight(self, pixel, value):
		if value == self._weightedPixel[0]:
			if self._weightedPixel[1] == 0.0:
				return self.weight + (self._weightedPixel[1] - self._weightedPixel[0]) * self.weight
			else:
				return self.weight + (self._weightedPixel[1] - self._weightedPixel[0]) / self._weightedPixel[1] * self.weight
		elif value == self._weightedPixel[2]:
			if self._weightedPixel[2] == 0.0:
				return self.weight - (self._weightedPixel[2] - self._weightedPixel[1]) * self.weight
			else:
				return self.weight - (self._weightedPixel[2] - self._weightedPixel[1]) / self._weightedPixel[2] * self.weight
		else:
			return self.weight
