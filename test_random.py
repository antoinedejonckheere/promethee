import utils;
import random;
import preference_functions;
#n_test = 10000;

#random_vector = [[random.random()] for x in range(n_test)];
#print random_vector;

#for x in range(n_test):
#	random_vector[x][0] = round(random_vector[x][0],2);

#utils.write_table_to_csv(random_vector, './random_dis.csv');

x = [-0.9,-0.4, -0.3, -0.01, 0.1, 0.3, 0.4, 0.5, 0.51, 0.89, 1.2];
y = []
for i in range(0, len(x)):
	y.append(preference_functions.preference_functions['quasi-criterion'](x[i]));

print y;
