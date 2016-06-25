# coding=utf-8

import utils
from promethee import Promethee
from promethee_simulation import prometheeSimulation

number_alternatives = 3;
number_criteria = 3;

# path where data needs to be written
path_to_file = './data/';

file_name = 'data_output.csv';

# preference functions to be considered
preference_functions = [
'linear',
'gaussian',
'quasi-criterion'];

# number of simulations to be run
number_simulations = 100000;

# number of decimals for RR frequency
ndigits = 5;


results_array = [];
results_array.append([
	'preference_function',
	'promethee I rr count',
	'frequency of promethee I',
	 'promethee II rr count',
	'frequency of promethee II']);

for preference_function in preference_functions:
	# initializes results array
	promethee_I_rr = utils.initialize_array(number_simulations);
	promethee_II_rr = utils.initialize_array(number_simulations);
	print preference_function;
	for simulation_number in range(number_simulations):
		promethee_simu = prometheeSimulation(number_alternatives, number_criteria, preference_function);
		promethee_I_rr[simulation_number] = promethee_simu.detect_promethee_I_rr();
		promethee_II_rr[simulation_number] = promethee_simu.detect_promethee_II_rr();
	## RR frequency for promethee I
	promethee_I_rr_frequency = utils.divide_integers(sum(promethee_I_rr), len(promethee_I_rr));
	print("number of ranks reversals for promethee I:")
	print(sum(promethee_I_rr));
	print("Promethee I rr frequency:");
	print promethee_I_rr_frequency;
	## RR frequency for promethee II
	promethee_II_rr_frequency = utils.divide_integers(sum(promethee_II_rr), len(promethee_II_rr));
	print("number of ranks reversals for promethee II:")
	print(sum(promethee_II_rr));
	print("Promethee II rr frequency:");
	print promethee_II_rr_frequency;
	results_array.append([
		preference_function, 
		sum(promethee_I_rr), 
		promethee_I_rr_frequency, 
		sum(promethee_II_rr), 
		promethee_II_rr_frequency]);

print results_array;

utils.write_table_to_csv(results_array, path_to_file+file_name);
