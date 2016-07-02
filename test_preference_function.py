# coding=utf-8

from preference_functions import PreferenceFunctions

p = 0.7;
q = 0.3;
sigma = 1;



pref_test_object = PreferenceFunctions(p, q, sigma);
pref_test = pref_test_object.get_preference_functions();

print("######################################")
print("Running tests for preference functions");
print("######################################")

print("USUAL function");
assert(pref_test['usual'](2) == 1);
assert(pref_test['usual'](-1)== 0);
print("Tests successful \n");

print("LINEAR function");
assert(pref_test['linear'](10) == 1);
assert(pref_test['linear'](0.8) == 1);
assert(pref_test['linear'](0.35) == 0.5);
print("Tests successful \n");

print("GAUSSIAN function");
assert(pref_test['gaussian'](0) == 0);
assert(pref_test['gaussian'](10000000) > 0.99)
assert(pref_test['gaussian'](-2) == 0);
print("Tests successful \n");

print("QUASI function");
assert(pref_test['quasi-criterion'](0)==0);
assert(pref_test['quasi-criterion'](0.301)==1);
assert(pref_test['quasi-criterion'](0.299)==0);
print("Tests successful \n");

print("LEVEL function");
assert(pref_test['level'](0.5) == 0.5);
assert(pref_test['level'](10) == 1);
assert(pref_test['level'](0.301) == 0.5);
assert(pref_test['level'](0.299) == 0);
assert(pref_test['level'](0.71) == 1);
assert(pref_test['level'](0.69) == 0.5);
print("Tests Successful \n");

print("LINEAR WITH INDIFFERENCE function");
assert(pref_test['linear_with_indifference'](0.29) == 0);
assert(pref_test['linear_with_indifference'](0.71) == 1);
assert(str(pref_test['linear_with_indifference'](0.5)) == '0.5');
print("Tests Successful \n");


print("#####################################");
print("Tests passed for preference functions");
print("#####################################");

