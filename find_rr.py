# coding=utf-8
import utils
import test_utils
from promethee import Promethee
from promethee_simulation import prometheeSimulation
import test_preference_function;
import test_promethee_model;
import test_promethee_simulation_class;
from preference_functions import generate_preference_function_parameters


number_criteria = 2;
number_alternatives = 3;
MAX_NUMBER_ITERATIONS = 1000000000000;

winning_alternative_3 = 0;
winning_alternative_4 = 0;

#weights = [0.5, 0.5];
preference_function = 'gaussian';
preference_function_parameters = {'p': 0, 'q': 0, 'sigma': 1};

continue_loop = True;
iterations_count = 0;

while winning_alternative_3 == winning_alternative_4:
    while continue_loop:
        iterations_count +=1;
        # define the experiment here
        promethee_simu = prometheeSimulation(number_alternatives, number_criteria, preference_function, preference_function_parameters);
        conditions_met = (promethee_simu.detect_promethee_I_rr() == 1 and 
                        promethee_simu.detect_promethee_II_rr()==1 and
                        promethee_simu.isLastAlternativeOutranked()) or iterations_count > MAX_NUMBER_ITERATIONS;
        if (conditions_met):
            continue_loop = False;

    print("Weights are");
    print(promethee_simu.get_weights());
    print("Evaluation table is");
    print(promethee_simu.get_evaluation_table());
    print("preference_function is");
    print preference_function;
    print("preference functions parameters are");
    print preference_function_parameters;
    print ('escaping after %s iterations')%iterations_count;

    print('running promethee methods for the set defined');
    evaluation_table = promethee_simu.get_evaluation_table();
    weights = promethee_simu.get_weights();
    promethee_object = Promethee(evaluation_table, weights, preference_function,preference_function_parameters);
    global_flow = promethee_object.getGlobalFlow();

    print('PROMETHEE II results');
    for elem in global_flow:
        print elem;
    winning_alternative_4 = global_flow.index(max(global_flow));
    print winning_alternative_4;

    promethee_object_removed = Promethee(evaluation_table[0:len(evaluation_table)-1],weights,preference_function,preference_function_parameters)
    global_flow_removed = promethee_object_removed.getGlobalFlow();
    print('######');
    for elem in global_flow_removed:
        print elem;
    winning_alternative_3 = global_flow_removed.index(max(global_flow_removed)); 
    print winning_alternative_3;

    print('#########################');
    print('PROMETHEE I results:')
    print('4 alternatives:');
    print promethee_object.getPrometheeIMatrix();
    print('3 alternatives: ')
    print promethee_object_removed.getPrometheeIMatrix();
    if winning_alternative_3==winning_alternative_4:
        continue_loop=True;

##Weights are
##[0.5317978414431725, 0.4682021585568274]
##Evaluation table is
##[[0.7419100000884347, 0.5299133923779944], [0.6091345210563468, 0.7937433257443319], [0.8705350222326868, 0.459129437942829], [0.2067642026291
##05, 0.3433499098184163]]
# gaussian, sigma = 1;
##escaping