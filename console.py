# -*- coding: utf-8 -*-

def header(title):
	print(u'----- {} -----'.format(title))

def stat(message, current, max):
	print('{} {}/{} ({:.2%})'.format(message, current, max, float(current) / float(max) if max else 0))

def confirm(message, defaultYes = False):
	acceptedAnswers = ['yes', 'ye', 'y']
	answer = choice(message, acceptedAnswers + ['no', 'n'], 'yes' if defaultYes else 'no')
	
	return answer in acceptedAnswers

def choice(message, options, default = None, invalidMessage = 'Value you entered is invalid'):
	answer = prompt(message, default).lower()

	while answer not in options:
		print(invalidMessage)
		answer = prompt(message, default).lower()

	return answer

def prompt(message, default = None):
	if default:
		message = '{} ({}): '.format(message, default)
	else:
		message = '{}: '.format(message)

	return input(message) or default
