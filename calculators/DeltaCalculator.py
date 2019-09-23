# -*- coding: utf-8 -*-
import abc

class DeltaCalculator:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def calculate(self, pixel, image):
		return
