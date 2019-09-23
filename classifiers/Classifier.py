# -*- coding: utf-8 -*-
import abc
import colorsys

class Classifier:
	__metaclass__ = abc.ABCMeta

	class ClassifiedImage:
		def __init__(self, image, r, g, b):
			h, s, v = colorsys.rgb_to_hsv(r, g, b)
			self.image = image
			self.r = r
			self.g = g
			self.b = b
			self.h = h
			self.s = s
			self.v = v

	@abc.abstractmethod
	def classify(self, images):
		return

	@abc.abstractmethod
	def classifyImage(self, images):
		return
