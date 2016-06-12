# coding=utf-8

import utils
from promethee import Promethee
from promethee_simulation import prometheeSimulation

number_alternatives = 3;
number_criteria = 2;

# number of simulations to be run
number_simulations = 1000;

# initializes results array
promethee_I_rr = utils.initialize_array(number_simulations);
promethee_II_rr = utils.initialize_array(number_simulations);

for simulation_number in range(number_simulations):
	promethee_simu = prometheeSimulation(number_alternatives, number_criteria);
	promethee_I_rr[simulation_number] = promethee_simu.detect_promethee_I_rr();
	promethee_II_rr[simulation_number] = promethee_simu.detect_promethee_II_rr();

#promethee_s = prometheeSimulation(number_alternatives, number_criteria);
#romethee_I_rr = promethee_s.detect_promethee_I_rr();

print promethee_I_rr;

print promethee_II_rr;

a = max(promethee_II_rr);
b = max(promethee_I_rr);

c = max(a,b);

print c;
print(a==b);