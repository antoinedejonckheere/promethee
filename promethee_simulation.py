# coding=utf-8

### this is the Promethee simulation class
### It creates a "promethee simulation object" that runs promethee models

import utils
from promethee import Promethee

class prometheeSimulation :
	def __init__(self, number_alternatives, number_criteria):
		self.number_criteria = number_criteria;
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