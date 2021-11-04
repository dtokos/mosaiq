# -*- coding: utf-8 -*-
import colorsys
from .DeltaCalculator import DeltaCalculator

class HSVDeltaCalculator(DeltaCalculator):
	def calculate(self, pixel, image):
		hsvPixel = self._toHSV(pixel)

		return float(
			self._hueDelta(hsvPixel, image) +
			self._saturationDelta(hsvPixel, image) +
			self._valueDelta(hsvPixel, image)
		) / 3.0

	def _toHSV(self, pixel):
		return list(colorsys.rgb_to_hsv(pixel[0], pixel[1], pixel[2]))

	def _hueDelta(self, pixel, image):
		return abs(image.h - pixel[0])

	def _saturationDelta(self, pixel, image):
		return abs(image.s - pixel[1])

	def _valueDelta(self, pixel, image):
		return abs(image.v - pixel[2])
