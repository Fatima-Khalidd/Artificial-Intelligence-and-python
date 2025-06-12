import random
# generate poppulation of random solutions (fibonachi calculator) 
def generate_population(pop_size,max_length):
    population=[]
    for _ in range(pop_size):
        individual=[random.randint(0,10) for _ in range(max_length) ] # random genes for each population
        population.append(individual)
    return population

# fitness function to evaluate the solution how accurate fibonacci number is
def fitness(individual):
    fibonacci= [0, 1,1,2,3,5,8,13,21,34] # correct fibonacci numbers, fitness should match this
    score=0
    for i in range(len(fibonacci)):
        predicted=individual[i]
        if predicted== fibonacci[i]:
            score+=1
    return score  

# selection function to select the best individuals based on fitness, select 2 individuals based on fitness
def selection(population):      
    population=sorted(population,key=lambda x: fitness(x),reverse=True)  # sort population based on fitness
    return population[:2]  # return top 2 individuals OR return population[0], population[1]


# crossover function to combine two parents to create a child
def crossover(parent1,parent2):
    crossover_point=len(parent1)//2  # crossover point is the middle of the parent
    child=parent1[:crossover_point] + parent2[:crossover_point]  # combine first half of parent1 and second half of parent2
    return child

# mutate an individual by changing a random gene
def mutate(individual):
    mutation_point=random.randint(0,len(individual) -1 )# select a random gene to mutate
    individual[mutation_point]=random.randint(0,10)  # change the gene to a random value
    return individual

# main function to run the genetic algorithm
def genetic_algorithm(pop_size,generations,max_length):
    population=generate_population(pop_size,max_length)  # generate initial population
    for generation in range(generations):
        print(f"Generation{generation+1}")
        parent1,parent2=selection(population)
        child=crossover(parent1,parent2)
        child=mutate(child)
        population.append(child)
        population=sorted(population,key=lambda x:fitness(x),reverse=True)[:pop_size]  # keep the population size constant
        print(f"Best fitness:{generation+1}:{fitness(population[0])}")
        print(f"Best individual:{population[0]}")

    return population[0]  # return the best individual after all generations

best_solution=genetic_algorithm(pop_size=10,generations=50,max_length=10)
print(f"Best final solution: {best_solution}")
# This code implements a simple genetic algorithm to evolve a population of individuals towards the Fibonacci sequence.
# The algorithm generates a population of random individuals, evaluates their fitness based on how closely they match the Fibonacci sequence, selects the best individuals, performs crossover to create new individuals, and mutates them to introduce variability. The process repeats for a specified number of generations, ultimately returning the best solution found.





