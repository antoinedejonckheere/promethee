import utils
from promethee import Promethee

number_alternatives = 3;
number_criteria = 2;

### initialize evaluation matrix

evaluation_table = utils.random_matrix(number_criteria, number_alternatives);
##### initialize weights for criteria
weights = utils.random_normalized_array(number_criteria);

# Define promethee I and promethee II matrices
promethee_init = Promethee(evaluation_table,weights);

# add one alternative
evaluation_table.append(utils.random_array(number_criteria));

#define new promethee object
promethee_final = Promethee(evaluation_table,weights);

#get promethee I and II ranking for both models
prometheeI_ranking_init = promethee_init.getPrometheeIMatrix();
prometheeII_ranking_init = promethee_init.getPrometheeIIMatrix();
prometheeI_ranking_final = promethee_final.getPrometheeIMatrix();
prometheeII_ranking_final = promethee_final.getPrometheeIIMatrix();

