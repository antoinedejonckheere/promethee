# coding=utf-8

import utils
from promethee import Promethee
from promethee_simulation import prometheeSimulation

number_alternatives = 3;
number_criteria = 3;

# number of simulations to be run
number_simulations = 10000;

# number of decimals for RR frequency
ndigits = 5;

# initializes results array
promethee_I_rr = utils.initialize_array(number_simulations);
promethee_II_rr = utils.initialize_array(number_simulations);

for simulation_number in range(number_simulations):
	promethee_simu = prometheeSimulation(number_alternatives, number_criteria,'linear');
	promethee_I_rr[simulation_number] = promethee_simu.detect_promethee_I_rr();
	promethee_II_rr[simulation_number] = promethee_simu.detect_promethee_II_rr();


print promethee_I_rr;

print promethee_II_rr;

print(promethee_I_rr == promethee_II_rr);

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
