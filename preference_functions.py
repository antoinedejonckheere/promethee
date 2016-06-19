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
		output = (delta)/1;
	return output;

preference_functions = {
	'usual': usual_function,
	'linear': linear_function
};