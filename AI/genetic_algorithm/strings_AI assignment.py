import random
  
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
  
    @staticmethod
    def mutated_genes():
        '''
        create random genes for mutation
        '''
        global GENES
        #Return a random element from a list or a sequence.
        gene = random.choice(GENES)
        return gene
  
    @staticmethod
    def create_gnome():
        '''
        create chromosome or string of genes
        '''
        global TARGET
        gnome_len = len(TARGET)
        return [Individual.mutated_genes() for _ in range(gnome_len)]
  
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
            if prob < 0.35: # 35% chance of getting a gene from parent 1
                child_chromosome.append(gp1)
  
            # if prob is between 0.45 and 0.90, insert
            # gene from parent 2
            elif prob < 0.85: # 50% chance of getting a gene from parent 2 # 85-35=50
                child_chromosome.append(gp2)
  
            #otherwise insert random gene(mutate), 
            #for maintaining diversity
            #the probability of mutation needs to be carefully tuned. 
            #Too big, you are probably not even going to get sufficiently close to a true solution
            #
            else: 
                child_chromosome.append(Individual.mutated_genes()) # mutation 15%
  
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
    
    @staticmethod
    def select(population, POPULATION_SIZE):
        new_generation = []
         #look over here
        s = int((10*POPULATION_SIZE)/100)
        new_generation.extend(population[:s]) 
  
        #look over here
        s = int((90*POPULATION_SIZE)/100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)

        return new_generation
  
# Driver code
def main():
    global POPULATION_SIZE
  
    #current generation
    generation = 1
  
    found = False
    population = []
  
    # create initial population
    for _ in range(POPULATION_SIZE):
                gnome = Individual.create_gnome()
                #you need gnome to create an individual. See how Individual class is defined
                population.append(Individual(gnome))
  
    while not found:
  
        # sort the population in increasing order of fitness score
        population = sorted(population, key = lambda x:x.fitness)
  
        # if the individual having lowest fitness score ie. 
        # 0 then we know that we have reached to the target
        # and break the loop
        if population[0].fitness <= 0:
            found = True
            break
  
        # # Otherwise generate new offsprings for new generation
        # new_generation = []
  
        # #look over here
        # s = int((10*POPULATION_SIZE)/100)
        # new_generation.extend(population[:s]) 
  
        # #look over here
        # s = int((90*POPULATION_SIZE)/100)
        # for _ in range(s):
        #     parent1 = random.choice(population[:50])
        #     parent2 = random.choice(population[:50])
        #     child = parent1.mate(parent2)
        #     new_generation.append(child)
  
        population = Individual.select(population, POPULATION_SIZE)
  
        print("Generation: {}\tString: {}\tFitness: {}".\
              format(generation,
              "".join(population[0].chromosome),
              population[0].fitness))
  
        generation += 1
  
      
    print("Generation: {}\tString: {}\tFitness: {}".\
          format(generation,
          "".join(population[0].chromosome),
          population[0].fitness))
  
if __name__ == '__main__':
    main()