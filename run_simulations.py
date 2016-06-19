from promethee import Promethee
import utils

# preferenceTable = [[1,2],
# [2,6],
# [3,4],
# [1,3]
# ];

# weights = [0.4, 0.6];

preferenceTable = [
[1,2],
[2,1],
[4,4]
];

weights = [0.5, 0.5];

Promethee(preferenceTable,weights,'usual');



####### Running tests before running simulation##########

test_preference_table=[
[4,2],
[1,5],
[3,4]
];

test_weights = [0.4, 0.6];

test_promethee = Promethee(test_preference_table, test_weights,'usual');

#### Define expected outcome of tests ######
expected_phi_plus = [0.4, 0.6, 0.5];
expected_phi_minus = [0.6, 0.4, 0.5];
expected_phi = [-0.2, 0.2, 0];

expected_pairwise_comparison_matrix=[
[0, 0.4, 0.4],
[0.6, 0, 0.6],
[0.6, 0.4, 0],];

expected_positive_matrix = [
[0,-1,-1],
[1,0,1],
[1,-1,0]
];

expected_negative_matrix=[
[0,-1,-1],
[1,0,1],
[1,-1,0]
];

expected_prometheeI_matrix = [
[0,-1,-1],
[1,0,1],
[1,-1,0]
];

expected_prometheeII_matrix = [
[0,-1,-1],
[1,0,1],
[1,-1,0]
];
###### Run tests ######


print("######################### \n Running tests \n #########################")
assert (test_promethee.phi_plus == expected_phi_plus);
assert (test_promethee.phi_minus == expected_phi_minus);
assert(test_promethee.pi == expected_pairwise_comparison_matrix);

assert(test_promethee.positive_matrix == expected_positive_matrix);
assert(test_promethee.negative_matrix == expected_negative_matrix);

assert(test_promethee.prometheeI_matrix == expected_prometheeI_matrix);
assert(test_promethee.prometheeII_matrix == expected_prometheeII_matrix);
print("######################### \n Tests passed \n #########################")
