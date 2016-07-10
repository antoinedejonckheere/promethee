from promethee_simulation import prometheeSimulation;


def run_promethee_simulation_tests():
	print("########################################################");
	print("########################################################");
	print("Running tests for promethee simulation class");
	print("########################################################");
	print("########################################################");
	print("\n");
	number_alternatives = 3;
	number_criteria = 2;
	matrix_init = [[1, 0, 'a'],['b', 1, 2],[2, 0, 0]];
	matrix_final = [[0,0,0],[0,0,0],[0,0,0]];
	matrix_final2 = matrix_init;
	promethee_simulation_test_object = prometheeSimulation(number_alternatives,number_criteria,'usual',{'p': 0, 'q': 0, 'sigma': 0});
	print("Testing COMPARE PROMETHEE MATRICES method");
	assert(promethee_simulation_test_object.compare_promethee_matrices(matrix_init, matrix_final)==False);
	assert(promethee_simulation_test_object.compare_promethee_matrices(matrix_init, matrix_final2)==True);
	print('\n');
	
	print("Testing COMPARE PROMETHEE I MATRICES method");
	matrix_init= [[0, 1, 'R'],[-1, 0, 0],['R', 0, 0]];
	matrix_final = [[0, 1, -1],[-1, 0, 'R'],[1, 'R', 0]];
	resulting = promethee_simulation_test_object.compare_promethee_I_matrices(matrix_init, matrix_final);
	assert(resulting['incomparability'] == 2);
	assert(resulting['preference_reversal']==0);
	matrix_final = [[0,-1,'R'],[1,0,0],['R',0,0]];
	resulting = promethee_simulation_test_object.compare_promethee_I_matrices(matrix_init, matrix_final);
	assert(resulting['incomparability'] == 0);
	assert(resulting['preference_reversal'] == 1);
	print('\n');
	
	print("Testing COMPARE PROMETHEE II MATRICES method");
	matrix_init=[[0,1,-1],[-1,0,1],[1,-1,0]];
	matrix_final=[[0, -1, -1],[1, 0, 1],[1, -1, 0]];
	resulting = promethee_simulation_test_object.compare_promethee_II_matrices(matrix_init,matrix_final);
	assert(resulting == 1);
	print('\n');


	print("########################################################");
	print("########################################################");
	print("Tests passed successfully for promethee simulation class");
	print("########################################################");
	print("########################################################");
	print("\n");

if __name__ == '__main__':
	run_promethee_simulation_tests();