# coding=utf-8

import utils
from promethee import Promethee
import promethee_simulation

number_alternatives = 3;
number_criteria = 2;


promethee_s = promethee_simulation.prometheeSimulation(number_alternatives, number_criteria);