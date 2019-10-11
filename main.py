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

	source = Image.open(sourceName).convert('RGBA')
	generator = makeGenerator(getTileImages(imagesPath))
	
	console.header('Generating')
	generatedImage = generator.generate(source)
	console.header('Saving')
	generatedImage.save(outputName, compress_level=1)

def getTileImages(imagesPath):
	return [Image.open(path).convert('RGBA') for path in glob.glob(os.path.join(imagesPath, '*.png'))]

def makeGenerator(images):
	classifier = AvgRGBClassifier()
	deltaCalculator = (
		AvgDeltaCalculator()
		.addCalculator(WeightedRGBDeltaCalculator(), 255.0)
		.addCalculator(WeightedHSVDeltaCalculator())
	)
	builder = Builder((56, 56))
	generator = Generator(classifier.classify(images), deltaCalculator, builder)

	return generator

if __name__ == '__main__':
	main()
