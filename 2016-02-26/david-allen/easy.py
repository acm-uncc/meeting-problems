## NOTICE ##
#	Major Contributor:	Parker Garrison
#	Author:			David Allen

import sys

# input from text file as cmd argument

class TempTracker():

	def __init__(self): 
		self.d = dict()
		self.themax = None;
		self.themin = None;
		self.themean = None;
		self.themode = None;
		self.sum = 0;
		self.length =  0;

	def insert(self, new_temp):
		if new_temp in self.d:
			self.d[new_temp] += 1;
			if self.d[new_temp] > self.d.get(self.themode, 0):
				self.themode = new_temp;
		else:
			self.d[new_temp] = 1;

		if (self.themax == None) or (new_temp > self.themax):
			self.themax = new_temp;

		if (self.themin == None) or (new_temp < self.themin):
			self.themin = new_temp;

		self.sum += new_temp;
		self.length += 1;
		self.themean = self.sum*1.0 / self.length;


	def get_max(self):
		return self.themax;
			
	def get_min(self):
		return self.themin;

	def get_mean(self):
		return self.themean;

	def get_mode(self):
		return self.themode;

temp_tracker = TempTracker();

with open( sys.argv[1] ) as file_input:
	for line in file_input:
		temp_tracker.insert( int(line) );
