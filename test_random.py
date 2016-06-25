import utils;
import random;

n_test = 10000;

random_vector = [[random.random()] for x in range(n_test)];
print random_vector;

for x in range(n_test):
	random_vector[x][0] = round(random_vector[x][0],2);

utils.write_table_to_csv(random_vector, './random_dis.csv');
