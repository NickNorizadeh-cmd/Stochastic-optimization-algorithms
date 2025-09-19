import math
from genetic_algorithm import run_function_optimization
import matplotlib.pyplot as plt

number_of_runs = 10                # Do NOT change
population_size = 100               # Do NOT change
maximum_variable_value = 5          # Do NOT change: (x_i in [-a,a], where a = maximumVariableValue)
number_of_genes = 50                # Do NOT change
number_of_variables = 2  	    # Do NOT change
tournament_size = 2                 # Do NOT change
tournament_probability = 0.75       # Do NOT change
crossover_probability = 0.8         # Do NOT change
number_of_generations = 50        # Do NOT change

mutation_probability_list = [0.0, 0.005, 0.01,0.02,0.05,0.1] # Add more values in this list; see the problem sheet

# Below you should add the required code for the statistical analysis 
# (computing median fitness values, and so on), as described in the problem sheet


list_of_medians = []
for mutation_probability in mutation_probability_list:
   list_of_max_fitness =[] # for every p_mut you should reset your list of maximum fitnesses

   for run_index in range(number_of_runs):
      #print("Bullshit")
      [maximum_fitness, x_best] = run_function_optimization(population_size, number_of_genes, number_of_variables, maximum_variable_value, tournament_size, \
                                       tournament_probability, crossover_probability, mutation_probability, number_of_generations);
   
      list_of_max_fitness.append(maximum_fitness)

   list_of_max_fitness.sort() # sort in place in ascending order
   n = len(list_of_max_fitness)
   if n % 2 == 0:
      median_after_100 = (list_of_max_fitness[n//2 - 1] + list_of_max_fitness[n//2])/2
   else:
      median_after_100 = list_of_max_fitness[n//2]
   list_of_medians.append(median_after_100)


print("p_mut listed is " , mutation_probability_list) # It runs until these two statements and prints them
print("list of medians for maximum fitness after 100 batch runs each", list_of_medians)


x = mutation_probability_list  
y = list_of_medians

# plot our list in X,Y coordinates
plt.scatter(x, y)
plt.plot(x, y, marker = '.', markersize = 10)
plt.show()



