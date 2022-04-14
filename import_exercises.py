# b. Within this file, use from to import the calculate_tip function directly. 
# Call this function with values you choose and print the result.
from functions_exercises import calculate_tip
calculate_tip(45, .20)

import itertools
# 2a. How many different ways can you combine the let
list(itertools.product('acbc', '123'))
# 2b. How many different combinations are there of 2 letters from "abcd"?
list(itertools.combinations('abcd', 2))
# 2c. How many different permutations are there of 2 letters from "abcd"?
list(itertools.permutations('abcd', 2))
