# coding=utf-8

import utils
import test_utils
from promethee import Promethee
from promethee_simulation import prometheeSimulation
import test_preference_function;
import test_promethee_model;
import test_promethee_simulation_class;
from preference_functions import generate_preference_function_parameters

def run_simulations():
	number_alternatives = 3;
	number_criteria = 2;

	# path where data needs to be written
	path_to_file = './data/';

	file_name = 'data_output';

	# preference functions to be considered
	preference_functions = [
	'usual',
	'quasi-criterion',
	'linear',
	'gaussian',
	'level',
	'linear_with_indifference'];

	# number of simulations to be run
	number_simulations = 1000;

	# number of decimals for RR frequency
	ndigits = 5;



	results_array = [];
	results_array.append([
		'preference_function',
		'p parameter',
		'q parameter',
		'sigma parameter',
		'promethee I rr count',
		'frequency of promethee I',
		 'promethee II rr count',
		'frequency of promethee II rr',
		'Preference reversal in promethee I count',
		'preference reversal in promethee I frequency',
		'incomparibilities reversal in promethee I count',
		'incomparaibilities reversal in promethee I frequency',
		'preference reversal in promethee II count',
		'preference reversal in promethee II frequency']);

	for preference_function in preference_functions:
		print "PREFERENCE FUNCTION:"
		print preference_function;
		print("###################");
		parameters_array = generate_preference_function_parameters(0.1, preference_function);
		for preference_function_parameters in parameters_array:
			# initializes results array
			promethee_I_rr = utils.initialize_array(number_simulations);
			promethee_II_rr = utils.initialize_array(number_simulations);
			promethee_I_pref_reversal = utils.initialize_array(number_simulations);
			promethee_I_incomparability = utils.initialize_array(number_simulations);
			promethee_II_rr_count = utils.initialize_array(number_simulations);
			for simulation_number in range(number_simulations):
				if (simulation_number%10000 == 0):
					print("Running simulation %s out of %s") %(simulation_number, number_simulations);
					#parameter_object = {'p':0.2, 'q': 0.1, 'sigma': 0.28};
				promethee_simu = prometheeSimulation(number_alternatives, number_criteria, preference_function, preference_function_parameters);
				promethee_I_rr[simulation_number] = promethee_simu.detect_promethee_I_rr();
				promethee_II_rr[simulation_number] = promethee_simu.detect_promethee_II_rr();
				dic = promethee_simu.specify_promethee_I_rr();
				promethee_I_pref_reversal[simulation_number] = dic['preference_reversal'];
				promethee_I_incomparability[simulation_number] = dic['incomparability']
				promethee_II_rr_count[simulation_number] = promethee_simu.specify_promethee_II_rr();
			## RR frequency for promethee I
			promethee_I_rr_frequency = utils.divide_integers(sum(promethee_I_rr), len(promethee_I_rr));
			print("number of ranks reversals for promethee I:")
			print(sum(promethee_I_rr));
			print("Promethee I rr frequency:");
			print promethee_I_rr_frequency;
			## rank reversal types for promethee I method
			promethee_I_preference_reversal = utils.divide_integers(sum(promethee_I_pref_reversal),len(promethee_I_pref_reversal));
			promethee_I_incomparability_freq = utils.divide_integers(sum(promethee_I_incomparability),len(promethee_I_incomparability));
			print("promethee I preference reversals:");
			print promethee_I_preference_reversal;
			print("promethee I incomparability change:");
			print promethee_I_incomparability_freq;
			## RR frequency for promethee II
			promethee_II_rr_frequency = utils.divide_integers(sum(promethee_II_rr), len(promethee_II_rr));
			print("number of ranks reversals in total order for promethee II:")
			print(sum(promethee_II_rr));
			print("Promethee II rr frequency:");
			print promethee_II_rr_frequency;
			## rr specifications for promethee II:
			promethee_II_rr_specs_frequency = utils.divide_integers(sum(promethee_II_rr_count),len(promethee_II_rr_count));
			print("Number of alternatives for which RR occurred in promethee II");
			print promethee_II_rr_specs_frequency;


			results_array.append([
				preference_function,
				preference_function_parameters['p'],
				preference_function_parameters['q'],
				preference_function_parameters['sigma'], 
				sum(promethee_I_rr), 
				promethee_I_rr_frequency, 
				sum(promethee_II_rr), 
				promethee_II_rr_frequency,
				sum(promethee_I_pref_reversal),
				promethee_I_preference_reversal,
				sum(promethee_I_incomparability),
				promethee_I_incomparability_freq,
				sum(promethee_II_rr_count),
				promethee_II_rr_specs_frequency]);


	print("PRINTING RESULTS");
	for result in results_array:
		print result;
		print("\n");

	print("WRITING results to file" + path_to_file+file_name);
	utils.write_table_to_csv(results_array, path_to_file+file_name+'_'+utils.generate_date_time_stamp()+".csv");

if __name__ == '__main__':
	test_preference_function.run_preference_functions_tests();
	test_promethee_model.run_promethee_test();
	test_utils.run_utils_tests();
	test_promethee_simulation_class.run_promethee_simulation_tests();
	run_simulations();
