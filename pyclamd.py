#!/usr/bin/env python

import os
import sys
from logging
import ConfigParser
from conf.conf import *

class PyClamd():
	#instance variables
	logger = None
	logformatter = None
	conf = None
	
	def __init__(self):
		self.inialiseLogging()
	
	def setConfig(self, configPath):
		config = ConfigParser.ConfigParser()
		config.read(configPath)
		self.conf = Conf(config)

		if self.conf.getLog() != None:
			self.setLogFile(self.conf.getLog)
		else:
			self.logger.fine("Not logging to file.")
	
	def setLogFile(self, logfile, loglevel=logging.DEBUG):
		fh = logging.FileHandler(logfile)
		fh.setLevel(loglevel)
		fh.setFormatter(self.formatter)
		self.logger.addHandler(fh)
		self.logger.fine("Logging to file '" + logfile + "'.")


	def inialiseLogging(self):
		# create logger
		self.logger = logging.getLogger('PyClamd')
		self.logger.setLevel(logging.DEBUG)

		# create formatter
		self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		
		# create console handler with a higher log level
		ch = logging.StreamHandler()
		ch.setLevel(logging.ERROR)

		ch.setFormatter(self.formatter)
	
		# add the handlers to the logger
		self.logger.addHandler(ch)
	



if __name__ == "__main__":
	main = PyClamd()
