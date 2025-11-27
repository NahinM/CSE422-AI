import random

class Element:
    def __init__(self,chromosome:list[int], fitVal:int) -> None:
        self.fitnessValue:int = fitVal
        self.Chromosome:list[int] = chromosome

    def fitness(self) -> None:
        global Data
        self.fitnessValue = 0
        weight = 0
        for i,v in enumerate(self.Chromosome):
            if self.Chromosome[i]==1:
                weight+=Data["weight"][i]
                self.fitnessValue+=Data["value"][i]
        if weight>Data["capacity"]: self.fitnessValue = -self.fitnessValue

    def mutate(self) -> None:
        N = len(self.Chromosome)
        self.Chromosome[random.randint(0,N-1)] = random.randint(0,1)

class Population:
    def __init__(self, populationSize:int, initialFitness:int) -> None:
        global Data
        chromosome:list[int] = [random.randint(0,1) for _ in range(Data["NumerOfItems"])]
        self.members:list[Element] = [ Element(chromosome,initialFitness) for _ in range(populationSize)]

    def select(self, fun) -> None:
        self.members = self.members[:min(fun(self.members),len(self.members))]

    def crossover(self,maxPopulationSize:int, crossoverLimit:int, crossoverPoint:int) -> None:
        newMembers:list[Element] = list()
        for p1 in range(len(self.members)):
            parent1_chromosome:list = self.members[p1].Chromosome
            for p2 in range(p1+1,min(len(self.members),p1+1+crossoverLimit)):
                parent2_chromosome:list = self.members[p2].Chromosome

                child1_chromosome = parent1_chromosome[:crossoverPoint] + parent2_chromosome[crossoverPoint:]
                child2_chromosome = parent2_chromosome[:crossoverPoint] + parent1_chromosome[crossoverPoint:]
                newMembers.append(Element(child1_chromosome,0))
                newMembers.append(Element(child2_chromosome,0))

                if len(newMembers)>=maxPopulationSize: break
            if len(newMembers)>=maxPopulationSize: break
        self.members = newMembers

    def fitness(self) -> None:
        for elm in self.members: elm.fitness()
        self.sort()
    
    def mutate(self) -> None:
        for elm in self.members: elm.mutate()

    def sort(self) -> None:
        self.members.sort(reverse=True, key=lambda elm: elm.fitnessValue)

    def bestValues(self, amount:int) -> list[Element]:
        return self.members[:min(amount,len(self.members))]
    
class AlgorithmRunner:
    def __init__(self, initialPopulationSize:int, maxPopulationSize:int, maxCrossoverLimit:int, crossoverPoint:int,initialFitness:int) -> None:
        self.InitialPopulationSize:int = initialPopulationSize
        self.MaxPopulationSize:int = maxPopulationSize
        self.SelectionFunction = lambda x: len(x)//2
        self.MaxCrossoverLimit:int = maxCrossoverLimit
        self.CrossoverPoint:int = crossoverPoint
        self.InitialFitness:int = initialFitness
    
    def run(self,generationLimit:int, bestValue:int) -> None:
        Generation:int = 0
        population:Population = Population(self.InitialPopulationSize,self.InitialFitness)
        population.fitness()
        while Generation<generationLimit:
            Generation+=1
            print(f"Generation No:{Generation}")

            population.select(self.SelectionFunction)
            population.crossover(self.MaxPopulationSize,self.MaxCrossoverLimit,self.CrossoverPoint)
            population.mutate()
            population.fitness()
            # if bestValue==population.bestValues(1)[0].fitnessValue: break

        print(population.bestValues(1)[0].Chromosome)

Data = {
    "capacity":5,
    "weight":[1,2,3],
    "value":[1,7,11],
    "NumerOfItems":3,
}

if __name__=="__main__":
    Algorithm:AlgorithmRunner = AlgorithmRunner(
        initialPopulationSize=80,
        maxPopulationSize=500,
        maxCrossoverLimit=10,
        crossoverPoint=2,
        initialFitness=0
    )

    Algorithm.run(generationLimit=10,bestValue=0)