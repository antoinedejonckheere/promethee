import utils

def usualShapeFunction(delta):
		if (delta>0):
			return 1;
		else:
			return 0;
class Promethee:
	def __init__(self,evaluationTable,weights):
		assert(len(weights)==len(evaluationTable[0]));
		self.evaluationTable = evaluationTable;
		self.numberAlternatives = len(evaluationTable);
		self.numberCriteria = len(evaluationTable[0]);
		self.weights = weights;
		self.normalizeWeights();
		self.assignShapeFunctions();
		print "this is a Promethee class with %s alternatives and %s criteria" %(self.numberAlternatives,self.numberCriteria)
		# compute pair wise comparison
		self.computePairWiseComparisonMatrix();
		self.computepositiveFlow();
		self.computeNegativeFlow();
		self.computeGlobalFlow();
		self.getPrometheeIIRanking();
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
		print("promethee II ranking \n")
		print("Global Promethee II scores are \n")
		for x in range(len(self.phi_global)):
			print (self.phi_global[x])
		self.prometheeII = sorted(range(len(self.phi_global)),key = lambda k: self.phi_global[k], reverse= True);
		print("ordered alternatives are:\n");
		for x in range(len(self.prometheeII)):
			print self.prometheeII[x];
	def getPrometheeIRanking(self):
		print("promethee I")
	def assignShapeFunctions(self):
		self.shapeFunction = [None]*self.numberCriteria;
		for i in xrange(self.numberCriteria):
			self.shapeFunction[i] = usualShapeFunction;
	def getPairwiseComparisonMatrix(self):
		self.computePairWiseComparisonMatrix();
		return self.pi;
	def computePairWiseComparisonMatrix(self):
		self.pi = utils.initialiseMatrix(self.numberAlternatives,self.numberAlternatives);
		for a in xrange(self.numberAlternatives):
			for b in xrange(self.numberAlternatives):
				if a!=b:
					sum = 0;
					for k in xrange(self.numberCriteria):
						delta = self.evaluationTable[a][k]-self.evaluationTable[b][k];
						sum += self.weights[k]*self.shapeFunction[k](delta);
					self.pi[a][b] = sum;
		print("Pairwise comparison matrix is")
		print self.pi;
