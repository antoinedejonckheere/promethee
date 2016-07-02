# coding=utf-8
from math import exp

Q = 0.5;

def usual_function(delta):
		if (delta>0):
			return 1;
		else:
			return 0;
def linear_function(delta):
	if (delta < 0):
		output = 0.0;
	elif (delta > 1):
		output = 1.0;
	else:
		output = (delta);
	return output;
def gaussian_function(delta):
	if (delta >0):
		res = exp(-(delta**2.0)/(2*(0.28**2)));
	else:
		res = 0;
	return res;

def quasi_criterion(delta):
	if delta > Q:
		res = 1;
	else:
		res = 0;
	return res;

def level_criterion(delta):
	if delta > 0 :
		if delta > 0.7:
			res = 1;
		elif delta > 0.3:
			res = 0.5;
		else:
			res = 0;
	else:
		res = 0;
	return res;

preference_functions = {
	'usual': usual_function,
	'linear': linear_function,
	'gaussian': gaussian_function,
	'quasi-criterion': quasi_criterion, 
	'level': level_criterion
};