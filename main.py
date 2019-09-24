# -*- coding: utf-8 -*-
import glob
from PIL import Image
from classifiers import AvgRGBClassifier
from Builder import Builder
from Generator import Generator
from calculators import AvgDeltaCalculator, WeightedRGBDeltaCalculator, WeightedHSVDeltaCalculator

def main():
	images = getTileImages()
	source = Image.open('source.png')
	classifier = AvgRGBClassifier()
	deltaCalculator = (
		AvgDeltaCalculator()
		.addCalculator(WeightedRGBDeltaCalculator(), 255.0)
		.addCalculator(WeightedHSVDeltaCalculator())
	)
	builder = Builder((56, 56))
	generator = Generator(classifier.classify(images), deltaCalculator, builder)
	generator.generate(source).save('output.png', compress_level=1)

def getTileImages():
	return [Image.open(path).convert('RGBA') for path in glob.glob('images/*.png')]


if __name__ == '__main__':
	main()
