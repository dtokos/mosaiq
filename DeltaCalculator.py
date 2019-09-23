# -*- coding: utf-8 -*-
import abc

class DeltaCalculator:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def calculate(self, pixel, image):
		return

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
		#print(maxValue, midValue, minValue, weigths)
		return weigths

class AvgDeltaCalculator(DeltaCalculator):
	def __init__(self):
		self._calculators = []
		self._weights = []

	def calculate(self, pixel, image):
		if len(self._calculators) == 0:
			raise 'No DeltaCalculators supplied'

		delta = 0;

		for index, calculator in enumerate(self._calculators):
			delta += calculator.calculate(pixel, image) * self._weights[index]

		return delta / len(self._calculators)

	def addCalculator(self, calculator, weigth = 1.0):
		self._calculators.append(calculator)
		self._weights.append(weigth)

		return self
