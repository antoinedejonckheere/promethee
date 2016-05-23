from promethee import Promethee
import utils

preferenceTable = [[1,2],
[2,6],
[3,4],
[1,3]
];

weights = [0.4, 0.6];

Promethee(preferenceTable,weights);