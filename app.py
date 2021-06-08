#!/usr/bin/env python3
try:
	import pywhatkit
except:
	print ("Error Importing pywhatkit")
	print ("Installing Latest Release of PyWhatKit from https://pypi.org")
	import pip
	pip.main(['install', 'pywhatkit'])

if __name__ == '__main__':
	print ("hello World!")
