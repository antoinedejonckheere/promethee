# coding=utf-8

### this is the Promethee simulation class
### It creates a "promethee simulation object" that runs promethee models

import utils
from promethee import Promethee

class prometheeSimulation :
	def __init__(self, number_alternatives, number_criteria, preference_function, parameters):
		self.number_criteria = number_criteria;
		self.number_alternatives = number_alternatives;
		self.evaluation_table = utils.random_matrix(number_criteria, number_alternatives);
		self.weights = utils.random_normalized_array(number_criteria);
		self.promethee_init = self.compute_promethee(preference_function, parameters);
		self.add_alternative();
		self.promethee_final = self.compute_promethee(preference_function, parameters);
	def compute_promethee(self, preference_function, parameters):
		promethee_object = Promethee(self.evaluation_table, self.weights, preference_function, parameters);
		return promethee_object;
	def add_alternative(self):
		self.evaluation_table.append(utils.random_array(self.number_criteria));
	def get_weights(self):
		return self.weights;
	def isLastAlternativeOutranked(self):
		# returns true if the last alternative is outranked by all the others
		# return false otherwise
		return_value = True;
		for x in range(0,self.number_criteria):
			criteria_evaluation= [];
			for y in range(0,self.number_alternatives+1):
				criteria_evaluation.append(self.evaluation_table[y][x]);
			if (criteria_evaluation.index(min(criteria_evaluation))!=self.number_alternatives):
				return_value = False;
		return return_value;
	def get_evaluation_table(self):
		return self.evaluation_table;
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
	def compare_promethee_I_matrices(self, matrix_init, matrix_final):
		# return the count of each rank reversal type
		# return value is stored in a dictionary
		rank_reversal = {
		'preference_reversal': 0, # aPb -> bPa, aIb->aPb, aPb ->aIb
		'incomparability': 0, # aPb -> aRb, aRb -> aPb
		};
		for x in range(self.number_alternatives):
			for y in range(self.number_alternatives):
				if matrix_init[x][y] != matrix_final[x][y]:
					if matrix_init[x][y] == 'R' or matrix_final[x][y]== 'R':
						rank_reversal['incomparability']+=1;
					else:
						rank_reversal['preference_reversal']+=1;
		rank_reversal['incomparability'] = rank_reversal['incomparability']/2;
		rank_reversal['preference_reversal']= rank_reversal['preference_reversal']/2;
		return rank_reversal;
	def compare_promethee_II_matrices(self, matrix_init, matrix_final):
		# return the count of alternatives for which RR has been observed
		# init variable
		count = 0;
		for x in range(self.number_alternatives):
			for y in range(self.number_alternatives):
				if matrix_init[x][y] != matrix_final[x][y]:
					count +=1;
		return count/2;
	def detect_promethee_I_rr(self):
		# returns 1 if rank reversal is observed in promethee I method
		promethee_I_rr = 0;
		if (self.compare_promethee_matrices(self.promethee_init.getPrometheeIMatrix(), self.promethee_final.getPrometheeIMatrix()) == False):
			promethee_I_rr = 1;
		return promethee_I_rr;
	def specify_promethee_I_rr(self):
		return self.compare_promethee_I_matrices(self.promethee_init.getPrometheeIMatrix(), self.promethee_final.getPrometheeIMatrix());
	def detect_promethee_II_rr(self):
		# returns 1 if rank reversal is observed in promethee II method
		promethee_II_rr = 0;
		if (self.compare_promethee_matrices(self.promethee_init.getPrometheeIIMatrix(), self.promethee_final.getPrometheeIIMatrix()) == False):
			promethee_II_rr = 1;
		return promethee_II_rr;
	def specify_promethee_II_rr(self):
		return self.compare_promethee_II_matrices(self.promethee_init.getPrometheeIIMatrix(), self.promethee_final.getPrometheeIIMatrix());

