# coding=utf-8

from preference_functions import PreferenceFunctions
import utils

def run_utils_tests():
	width = 3;
	height = 2;


	print("######################################")
	print("###Running tests for utils package####");
	print("######################################")

	print("initialize matrix method");
	test1 = utils.initialise_matrix(width,height)
	assert(max(max(test1)) == 0);
	assert(len(test1)==height);
	assert(len(test1[0])==width);

	print("#####################################");
	print("###Tests passed for utils package####");
	print("#####################################");
	print("\n");

if __name__ == '__main__':
	run_utils_tests();

