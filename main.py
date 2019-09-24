# -*- coding: utf-8 -*-
import os
import glob
import console
from PIL import Image
from classifiers import AvgRGBClassifier
from Builder import Builder
from Generator import Generator
from calculators import AvgDeltaCalculator, WeightedRGBDeltaCalculator, WeightedHSVDeltaCalculator

def main():
	imagesPath = console.prompt('Enter images path', './images/')
	sourceName = console.prompt('Enter source', 'source.png')
	outputName = console.prompt('Enter source', 'output.png')

	images = getTileImages(imagesPath)
	source = Image.open(sourceName)
	classifier = AvgRGBClassifier()
	deltaCalculator = (
		AvgDeltaCalculator()
		.addCalculator(WeightedRGBDeltaCalculator(), 255.0)
		.addCalculator(WeightedHSVDeltaCalculator())
	)
	builder = Builder((56, 56))
	generator = Generator(classifier.classify(images), deltaCalculator, builder)
	generator.generate(source).save(outputName, compress_level=1)

def getTileImages(imagesPath):
	return [Image.open(path).convert('RGBA') for path in glob.glob(os.path.join(imagesPath, '*.png'))]


if __name__ == '__main__':
	main()
