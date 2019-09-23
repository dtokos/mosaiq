# -*- coding: utf-8 -*-
from DeltaCalculator import DeltaCalculator

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
