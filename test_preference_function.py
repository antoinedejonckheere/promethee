# coding=utf-8

from preference_functions import PreferenceFunctions
from preference_functions import generate_preference_function_parameters;


def run_preference_functions_tests():
	p = 0.7;
	q = 0.3;
	sigma = 1;

	pref_test_object = PreferenceFunctions(p, q, sigma);
	pref_test = pref_test_object.get_preference_functions();

	print("######################################")
	print("Running tests for preference functions");
	print("######################################")

	print("USUAL function");
	assert(pref_test['usual'](2) == 1);
	assert(pref_test['usual'](-1)== 0);
	print("Tests successful \n");

	print("LINEAR function");
	assert(pref_test['linear'](10) == 1);
	assert(pref_test['linear'](0.8) == 1);
	assert(pref_test['linear'](0.35) == 0.5);
	print("Tests successful \n");

	print("GAUSSIAN function");
	assert(pref_test['gaussian'](0) == 0);
	assert(pref_test['gaussian'](10000000) > 0.99)
	assert(pref_test['gaussian'](-2) == 0);
	print("Tests successful \n");

	print("QUASI function");
	assert(pref_test['quasi-criterion'](0)==0);
	assert(pref_test['quasi-criterion'](0.301)==1);
	assert(pref_test['quasi-criterion'](0.299)==0);
	print("Tests successful \n");

	print("LEVEL function");
	assert(pref_test['level'](0.5) == 0.5);
	assert(pref_test['level'](10) == 1);
	assert(pref_test['level'](0.301) == 0.5);
	assert(pref_test['level'](0.299) == 0);
	assert(pref_test['level'](0.71) == 1);
	assert(pref_test['level'](0.69) == 0.5);
	print("Tests Successful \n");

	print("LINEAR WITH INDIFFERENCE function");
	assert(pref_test['linear_with_indifference'](0.29) == 0);
	assert(pref_test['linear_with_indifference'](0.71) == 1);
	assert(str(pref_test['linear_with_indifference'](0.5)) == '0.5');
	print("Tests Successful \n");


	print("#####################################");
	print("Tests passed for preference functions");
	print("#####################################");
	print("\n");

	print("########################################")
	print("Running tests for parameters generation");
	print("########################################")
	print("\n");

	test_obj = generate_preference_function_parameters(0.1,'usual');
	assert(test_obj== [{'p':0, 'q':0, 'sigma': 0}]);

	test_obj = generate_preference_function_parameters(0.1,'linear');
	assert(len(test_obj)==10);

	test_obj = generate_preference_function_parameters(0.1,'quasi-criterion');
	assert(len(test_obj)==10);

	def return_p(elem):
		return elem['p'];
	def return_q(elem):
		return elem['q'];
	def return_sigma(elem):
		return elem['sigma'];

	q_array = map(return_q, test_obj);

	assert(min(q_array) == 0);
	assert(max(q_array) == 0.9);


	print("########################################")
	print("Tests passed for parameters generation");
	print("########################################")
if __name__ == '__main__':
	run_preference_functions_tests();

