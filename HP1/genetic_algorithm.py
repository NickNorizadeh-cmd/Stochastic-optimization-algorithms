import random
from random import sample
import math

def g(x1, x2):
    term1 = (1.5 - x1 + x1 * x2) ** 2
    term2 = (2.25 - x1 + x1 * (x2 ** 2)) ** 2
    term3 = (2.625 - x1 + x1 * (x2 ** 3)) ** 2
    return term1 + term2 + term3

# Insertion sort in Python
def insertion_sort(arr):
  for step in range(1, len(arr)):
    key = arr[step]
    j = step - 1
    while j >= 0 and key > arr[j]:
  # For ascending order, change key> arr[j] to key < arr[j].
     arr[j + 1] = arr[j]
     j = j - 1
     arr[j + 1] = key

# Initialize population:
# Uncomment the line below and implement the function
def initialize_population (population_size, number_of_genes):
    population = [[random.randint(0,1) for gene_index in range (number_of_genes)]
                            for chromosome_index in range(population_size)]

    return population  
    
# Decode chromosome:
# Note: the variables should each take values in the range [-a,a], where a = maximum_variable_value
# Uncomment the line below and implement the function
def decode_chromosome(chromosome,nr_of_variables,variable_range):
    m = len(chromosome)
    k = m//nr_of_variables # k = m/ n - nr of genes (bits) per variable 
    x = 0
    j = 0
    i = 0
    x_temp = 0
    x_temp_list = []
    x_variables = [] # List of the 
    while j < m:
       x_temp += chromosome[j] * pow(2,-i-1) # skapar summan 2^-i*g_i korrekt
       i+=1
       if(i==k):
          x_temp_list.append(x_temp)
          x_temp = 0
          i = 0
       j+=1

    for i in range (nr_of_variables):
       x_variables.append(-variable_range + (2*variable_range*x_temp_list[i]/(1-pow(2,-k))))

    return x_variables

# Evaluate indviduals:
# Note: You may hard-code the evaluation of the fitness (g(x_1,g_x2)+1)^(-1)) here
# Uncomment the line below and implement the function
def evaluate_individual(x):
   x_1 = x[0]
   x_2 = x[1]
   sum = g(x_1,x_2) + 1

   return pow(sum, -1)


# Select individuals:
# Uncomment the line below and implement the function

import random
from random import sample

def tournament_select(fitness_list, tournament_probability, tournament_size):
    if len(fitness_list) == 0:
        print("Fitness list is empty")
        return None  
    
    if tournament_size == 0:
        print("Tournament size is 0")
        return None  
    
    indices = list(range(len(fitness_list))) # Generate a list of indices for the indices of fitness_list
    randomly_selected_indices = sample(indices, tournament_size) # randomly select j indices from the indices list
    
    # sort the j indices by fitness (descending)
    tournament_indices = sorted(randomly_selected_indices, key=lambda idx: fitness_list[idx], reverse=True) 
    
    last_index = None 
    while len(tournament_indices) > 0:
        last_index = tournament_indices[0]
        r = random.random()
        if r < tournament_probability:
            return last_index
        else:
            del tournament_indices[0]
                
    return last_index

# Carry out crossover:
# Uncomment the line below and implement the function
def cross (chromosome1,chromosome2):
    number_of_genes = len(chromosome1)
    cross_point = random.randint(1,number_of_genes-1)

    new_chromosome_1 = chromosome1 [:cross_point] + chromosome2[cross_point:]
    new_chromosome_2 = chromosome2[:cross_point] + chromosome1[cross_point:]

    return [new_chromosome_1, new_chromosome_2]

# Mutate individuals:
# Uncomment the line below and implement the function
def mutate (chromosome, mutation_probability):

    number_of_genes = len(chromosome)
    mutated_chromosome = chromosome.copy()
    for gene_index in range(number_of_genes):
        r = random.random()
        if(r < mutation_probability):
            mutated_chromosome[gene_index] = 1-chromosome[gene_index]
    return mutated_chromosome

# Genetic algorithm

def run_function_optimization(population_size, number_of_genes, number_of_variables, maximum_variable_value, \
                              tournament_size, tournament_probability, crossover_probability,\
                              mutation_probability, number_of_generations):
 
 # This function should return the maximum fitness and the best individual (i.e., a vector with
 # two elements (x1,x2) containing the values corresponding to the maximum fitness found.
 
 # Note that some parameters have different names compared to the programming introduction

  population = initialize_population(population_size,number_of_genes)

  for generation_index in range(number_of_generations):
    maximum_fitness = 0
    best_chromosome = []
    best_individual = []
    fitness_list = []
    for chromosome in population:
      individual = decode_chromosome(chromosome,number_of_variables,maximum_variable_value)
      fitness = evaluate_individual(individual)
      if (fitness > maximum_fitness):
        maximum_fitness = fitness
        best_chromosome = chromosome.copy()  
        best_individual = individual.copy()
      fitness_list.append(fitness)

    temp_population = []
    for i in range(0,population_size,2):
      index_1 = tournament_select(fitness_list, tournament_probability, tournament_size)
      index_2 = tournament_select(fitness_list, tournament_probability, tournament_size)
      chromosome1 = population[index_1].copy()
      chromosome2 = population[index_2].copy()
      r = random.random()
      if r < crossover_probability:
        [new_chromosome_1, new_chromosome_2] = cross(chromosome1,chromosome2)
        temp_population.append(new_chromosome_1)
        temp_population.append(new_chromosome_2) 
      else:
        temp_population.append(chromosome1)
        temp_population.append(chromosome2)

    for i in range(population_size):
      original_chromosome = temp_population[i]

      mutated_chromosome = mutate(original_chromosome, mutation_probability)
      temp_population[i] = mutated_chromosome

    temp_population[0] = best_chromosome
    population = temp_population.copy()

  return [maximum_fitness, best_individual]
 
# Decode chromosome test and evaluate individual test
#test_chromosome = [0,1,0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0]
#test_variable_number = 2
#test_variable_range = 3
#x_res = decode_chromosome(test_chromosome,test_variable_number,test_variable_range)

#print(evaluate_individual(x_res))

# Insertion sort test
#arr = [15, 68, -27, -4, 10,97,-3]
#insertion_sort(arr)
#print('Sorted Array in descending Order:')
#print(arr)

# Tournament selection test

#print("Randomly selected list of indices", randomly_selected_indices)
#print("Randomly torunament list of fitnessses in descending order", tournament_indices)

# Check to show that the fitness list is a tuple
#print("Sample fitness_list contents:")
#for i, x in enumerate(fitness_list):
#print(i, x, type(x))

p_tour = 0.7
j = 3
#fitness_test_list = []
fitness_test_list = [6,19,11,2]
#returned_individual = tournament_select(fitness_test_list, p_tour, j)
#print("Returned individual is: " , returned_individual)

#results = []
#for _ in range(10):
#    winner_index = tournament_select(fitness_test_list, p_tour, j)
#    winner_fitness = fitness_test_list[winner_index]
#    results.append((winner_index, winner_fitness))

#print("Tournament results (index, fitness):")
#for res in results:
#    print(res)
