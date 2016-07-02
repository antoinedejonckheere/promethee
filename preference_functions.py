# coding=utf-8
from math import exp

class PreferenceFunctions:
	def __init__(self, p, q, sigma):
		self.p = p;
		self.q = q;
		self.sigma = sigma;
	def usual_function(self, delta):
		if (delta>0):
			return 1;
		else:
			return 0;	
	def linear_function(self, delta):
		if (delta < 0):
			output = 0.0;
		elif (delta <self.p):
			output = delta/self.p;
		elif (delta > self.p):
			output = 1.0;
		else:
			output = (delta);
		return output;
	
	def gaussian_function(self, delta):
		if (delta >0):
			res = exp(-(delta**2.0)/(2*(self.sigma**2)));
		else:
			res = 0;
		return res;
	
	def quasi_criterion(self, delta):
		if delta >self.q:
			res = 1;
		else:
			res = 0;
		return res;

	def level_criterion(self, delta):
		if delta > 0 :
			if delta > self.p:
				res = 1;
			elif delta > self.q:
				res = 0.5;
			else:
				res = 0;
		else:
			res = 0;
		return res;
	def linear_with_indifference(self, delta):
		if delta < self.q:
			res = 0;
		else:
			if delta > self.p:
				res = 1;
			else:
				res = (delta -self.q)/(self.p-self.q);
		return res;

	def get_preference_functions(self):
		return {
			'usual': self.usual_function,
			'linear': self.linear_function,
			'gaussian': self.gaussian_function,
			'quasi-criterion': self.quasi_criterion, 
			'level': self.level_criterion,
			'linear_with_indifference': self.linear_with_indifference
		}
