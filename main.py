# -*- coding: utf-8 -*-
import glob
from PIL import Image
from Builder import Builder
from Generator import Generator

def main():
	images = getTileImages()
	source = Image.open('source.png')
	builder = Builder()
	generator = Generator(images, builder)
	generator.generate(source).save('output.png')

def getTileImages():
	return [Image.open(path).convert('RGBA') for path in glob.glob('images/*.png')]


if __name__ == '__main__':
	main()
