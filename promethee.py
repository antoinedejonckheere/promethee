# coding=utf-8
import utils
from preference_functions import * 

class Promethee:
	# defines the promethee class that we will use to run simulation
	# evalutionTable (array): table of evaluation of the alternatives w.r.t criteria
	# weights (vector): weights for the criteria
	# preference function : type of preference function given (string)
	def __init__(self,evaluationTable,weights, preference_function):
		assert(len(weights)==len(evaluationTable[0]));
		self.evaluationTable = evaluationTable;
		self.numberAlternatives = len(evaluationTable);
		self.numberCriteria = len(evaluationTable[0]);
		self.weights = weights;
		self.normalizeWeights();
		self.preference_function = preference_function;
		self.assignShapeFunctions();
		# print "this is a Promethee class with %s alternatives and %s criteria" %(self.numberAlternatives,self.numberCriteria)
		# compute pair wise comparison
		self.computeAllRankings();
	def computeAllRankings(self):
		self.computePairWiseComparisonMatrix();
		self.computepositiveFlow();
		self.computeNegativeFlow();
		self.computeGlobalFlow();
		self.computePositiveMatrix();
		self.computeNegativeMatrix();
		self.computePrometheeIMatrix();
		self.computePrometheeIIMatrix();
	def normalizeWeights(self):
		# normalizes the weights given as an input;
		sumW = sum(self.weights);
		for i in range(len(self.weights)):
			self.weights[i] = self.weights[i]/sumW;
	def computepositiveFlow(self):
		phi_plus = [0]*self.numberAlternatives;
		for a in xrange(self.numberAlternatives):
			sum = 0;
			for b in xrange(self.numberAlternatives):
				sum += self.pi[a][b];
			phi_plus[a] = sum/(self.numberAlternatives-1);
		self.phi_plus = phi_plus;
	def computeNegativeFlow(self):
		phi_minus = [0]*self.numberAlternatives;
		for a in xrange(self.numberAlternatives):
			sum = 0;
			for b in xrange(self.numberAlternatives):
				sum += self.pi[b][a];
			phi_minus[a] = sum/(self.numberAlternatives-1);
		self.phi_minus = phi_minus;
	def computeGlobalFlow(self):
		self.phi_global = [0]*self.numberAlternatives;
		for a in xrange(self.numberAlternatives):
			self.phi_global[a] = self.phi_plus[a]-self.phi_minus[a];
	def getPrometheeIIRanking(self):
		#print("promethee II ranking \n")
		#print("Global Promethee II scores are \n")
		for x in range(len(self.phi_global)):
			print (self.phi_global[x])
		self.prometheeII = sorted(range(len(self.phi_global)),key = lambda k: self.phi_global[k], reverse= True);
		#print("ordered alternatives are:\n");
		for x in range(len(self.prometheeII)):
			print self.prometheeII[x];
	def getPrometheeIRanking(self):
		print("promethee I")
	def assignShapeFunctions(self):
		self.shapeFunction = [None]*self.numberCriteria;
		assert(self.preference_function in preference_functions);
		for i in xrange(self.numberCriteria):
			self.shapeFunction[i] = preference_functions[self.preference_function];
	def getPairwiseComparisonMatrix(self):
		self.computePairWiseComparisonMatrix();
		return self.pi;
	def computePairWiseComparisonMatrix(self):
		self.pi = utils.initialise_matrix(self.numberAlternatives,self.numberAlternatives);
		for a in xrange(self.numberAlternatives):
			for b in xrange(self.numberAlternatives):
				if a!=b:
					sum = 0;
					for k in xrange(self.numberCriteria):
						delta = self.evaluationTable[a][k]-self.evaluationTable[b][k];
						sum += self.weights[k]*self.shapeFunction[k](delta);
					self.pi[a][b] = sum;
		#print("Pairwise comparison matrix is")
		#print self.pi;
	def computePositiveMatrix(self):
		self.positive_matrix = utils.initialise_matrix(self.numberAlternatives,self.numberAlternatives);
		for a in xrange(self.numberAlternatives):
			for b in xrange(self.numberAlternatives):
				if self.phi_plus[a]>self.phi_plus[b]:
					self.positive_matrix[a][b] = 1;
				elif self.phi_plus[a]<self.phi_plus[b]:
					self.positive_matrix[a][b] = -1;
				else:
					self.positive_matrix[a][b] = 0;
		#for a in xrange(self.numberAlternatives):
		#	for b in xrange(self.numberAlternatives):
				#print("Alternative %s with positive flow %s \n") %(a,self.phi_plus[a]);
				#print("Alternative %s with positive flow %s \n") %(b,self.phi_plus[b]);
				#print("making positive matrix element of %s \n") %(self.positive_matrix[a][b]);
				#print("########################################");
	def computeNegativeMatrix(self):
		self.negative_matrix = utils.initialise_matrix(self.numberAlternatives,self.numberAlternatives);
		for a in xrange(self.numberAlternatives):
			for b in xrange(self.numberAlternatives):
				if self.phi_minus[a]<self.phi_minus[b]:
					self.negative_matrix[a][b] = 1;
				elif self.phi_minus[a]>self.phi_minus[b]:
					self.negative_matrix[a][b] = -1;
				else:
					self.negative_matrix[a][b] = 0;
		#for a in xrange(self.numberAlternatives):
		#	for b in xrange(self.numberAlternatives):
				#print("Alternative %s with negative flow %s \n") %(a,self.phi_minus[a]);
				#print("Alternative %s with negative flow %s \n") %(b,self.phi_minus[b]);
				#print("making negative matrix element of %s \n") %(self.negative_matrix[a][b]);
				#print("########################################");
	def computePrometheeIMatrix(self):
		self.prometheeI_matrix = utils.initialise_matrix(self.numberAlternatives,self.numberAlternatives);
		for a in range(self.numberAlternatives):
			for b in range(self.numberAlternatives):
				# cas 1 : les deux flux donnent le même résultat
				# en conséquence, le ranking promethee I est équivalent au ranking de chacun des flux positif
				# et négatif
				# ceci couvre les cas : double préférence, double indifférence
				if (self.positive_matrix[a][b] == self.negative_matrix[a][b]):
					self.prometheeI_matrix[a][b] = self.positive_matrix[a][b]
				# cas 2: on doit gérer la présence d'une indifférence
				else:
					# cas 1: l'un des deux classements donne une égalité.
					# dans ce cas, le ranking est la somme des deux rankings
					if (self.positive_matrix[a][b]==0 or self.negative_matrix[a][b]==0):
						self.prometheeI_matrix[a][b]= self.positive_matrix[a][b]+self.negative_matrix[a][b];
					# dernier cas: les deux resultats sont différents et aucun n'est nul. Donc, incomparabilité!
					else:
						self.prometheeI_matrix[a][b] = "R";
	def computePrometheeIIMatrix(self):
		self.prometheeII_matrix = utils.initialise_matrix(self.numberAlternatives,self.numberAlternatives);
		for a in range(self.numberAlternatives):
			for b in range(self.numberAlternatives):
				if self.phi_plus[a]>self.phi_plus[b]:
					self.prometheeII_matrix[a][b]=1;
				elif self.phi_plus[a]<self.phi_plus[b]:
					self.prometheeII_matrix[a][b]=-1;
				else:
					self.prometheeII_matrix[a][b]=0;
	def getPrometheeIIMatrix(self):
		return self.prometheeII_matrix;
	def getPrometheeIMatrix(self):
		return self.prometheeI_matrix;
	def getPositiveMatrix(self):
		return self.positive_matrix;
	def getNegativeMatrix(self):
		return self.negative_matrix;
	def getPairwiseComparisonMatrix(self):
		return self.pi;