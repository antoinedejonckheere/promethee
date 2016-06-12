# coding=utf-8

### this is the Promethee simulation class
### It creates a "promethee simulation object" that runs promethee models

import utils
from promethee import Promethee

class prometheeSimulation :
	def __init__(self, number_alternatives, number_criteria):
		self.number_criteria = number_criteria;
		self.number_alternatives = number_alternatives;
		self.evaluation_table = utils.random_matrix(number_criteria, number_alternatives);
		self.weights = utils.random_normalized_array(number_criteria);
		self.promethee_init = self.compute_promethee();
		self.add_alternative();
		self.promethee_final = self.compute_promethee();
	def compute_promethee(self):
		promethee_object = Promethee(self.evaluation_table, self.weights);
		return promethee_object;
	def add_alternative(self):
		self.evaluation_table.append(utils.random_array(self.number_criteria));
	def compare_promethee_matrices(self, matrix_init, matrix_final):
		# return true if both matrices are the same
		# false otherwise
		ret = True;
		for x in range(self.number_alternatives):
			for y in range(self.number_alternatives):
				if matrix_init[x][y] != matrix_final[x][y]:
					ret = False;
					break;
		return ret;
	def detect_promethee_I_rr(self):
		promethee_I_rr = 0;
		if (self.compare_promethee_matrices(self.promethee_init.getPrometheeIMatrix(), self.promethee_final.getPrometheeIMatrix()) == False):
			promethee_I_rr = 1;
		return promethee_I_rr;
	def detect_promethee_II_rr(self):
		promethee_II_rr = 0;
		if (self.compare_promethee_matrices(self.promethee_init.getPrometheeIIMatrix(), self.promethee_final.getPrometheeIIMatrix()) == False):
			promethee_II_rr = 1;
		return promethee_II_rr;