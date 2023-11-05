import random
import numpy as np
import matplotlib.pyplot as plt
  
# Number of individuals in each generation
POPULATION_SIZE = 100
  
# Valid genes
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@$'{[]}'''
  
# Target string to be generated
TARGET = "CS 335 AI is real fun...sometimes maybe a little challengin', but I love it!"
  
class Individual(object):
    '''
    Class representing individual in population
    '''
    def __init__(self, chromosome):
        self.chromosome = chromosome 
        self.fitness = self.cal_fitness()
        
    def __repr__(self):
        return  f'chromosome is {self.chromosome},fitness is {self.fitness}' 
  
    @classmethod
    def mutated_genes(self):
        '''
        create random genes for mutation
        '''
        global GENES
        #Return a random element from a list or a sequence.
        gene = random.choice(GENES)
        return gene
  
    @classmethod #this is meant to be a factory method. It is...poorly written. I'll admit.
    def create_gnome(self):
        '''
        create chromosome or string of genes
        '''
        global TARGET
        gnome_len = len(TARGET)
        return [self.mutated_genes() for _ in range(gnome_len)]
  
    def mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''
  
        # chromosome for offspring
        child_chromosome = []
        #this is a pretty neat construct using zip. zip of two lists.
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):    
  
            # random probability
            #Almost all module functions depend on the basic function random(), #
            # which generates a random float uniformly in the half-open range 0.0 <= X < 1.0.  
            prob = random.random()
  
            #note here the rule is pretty 'arbitrary'. GA is heuristic. Rules are not strictly defined.
            # if prob is less than 0.45, insert gene
            # from parent 1 
            if prob < 0.475:
                child_chromosome.append(gp1)
  
            # if prob is between 0.475 and 0.95, insert
            # gene from parent 2
            elif prob < 0.95:
                child_chromosome.append(gp2)
  
            #otherwise insert random gene(mutate), 
            #for maintaining diversity
            #the probability of mutation needs to be carefully tuned. 
            #Too big, you are probably not even going to get sufficiently close to a true solution
            #
            else:
                child_chromosome.append(self.mutated_genes())
  
        # create new Individual(offspring) using 
        # generated chromosome for offspring
        return Individual(child_chromosome)
  
    def cal_fitness(self):
        '''
        Calculate fitness score, it is the number of
        characters in string which differ from target
        string.
        '''
        global TARGET
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET):
            if gs != gt:
                fitness+= 1
        return fitness
  
# Driver code
def main():
    global POPULATION_SIZE
  
    #current generation
    generation = 1
  
    #found = False
    population = []

    # Initialize list to store best fitness values for each generation
    list_fitness = []
  
    # create initial population
    for _ in range(POPULATION_SIZE):
                gnome = Individual.create_gnome()
                #you need gnome to create an individual. See how Individual class is defined
                population.append(Individual(gnome))
  
    for generation in range(5000):
  
        # sort the population in increasing order of fitness score
        population = sorted(population, key = lambda x:x.fitness)
  
         # store the best fitness value for this generation
        best_individual_fitness = population[0].fitness
        list_fitness.append(best_individual_fitness)

        # if the best individual of a certain generation has a fitness of 0,
        # then we know that we have reached to the target
        # and will break the loop
        # if population[0].fitness <= 0:
        #     found = True
        #     break
  
        # Otherwise generate new offsprings for new generation
        new_generation = []
  
        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation...#
        # They are so fit that their exact clones are considered part of the next generation 
        s = int((10*POPULATION_SIZE)/100)
        new_generation.extend(population[:s])
  
        # From 50% of fittest population, Individuals 
        # will mate/crossover to produce offspring. Again, these more-than-average get to crossover multiple times to 
        #produce new individuals that make part of the new generation.  
        s = int((90*POPULATION_SIZE)/100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)
  
        population = new_generation
  
        generation += 1
  
      
    # print("Generation: {}\tString: {}\tFitness: {}".\
    #       format(generation,
    #       "".join(population[0].chromosome),
    #       population[0].fitness))

    # Plot the fitness values for each generation
    Y_test = np.array(list_fitness)
    print(Y_test)
    X_test = np.arange(5000)
    plt.plot(X_test,Y_test)
    plt.show()

'''
The shape of the graph resembles a Elbow graph, which is basically a plot of
fitness values for each of the generations. X represents the generation number
and y represents the fitness. We can see that the fitness value decreases as 
the generation number increases. The generations are becoming more and mroe fit 
for their environment, but are eventually converging to a local optimum value.

'''  
if __name__ == '__main__':
    main()