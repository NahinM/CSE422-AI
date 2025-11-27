import random

class Element:
    def __init__(self,chromosome:list, fitVal:int) -> None:
        self.fitnessValue:int = fitVal
        self.Chromosome:list = chromosome

    def fitness(self) -> None:
        self.fitnessValue = 0
        for col1 in range(len(self.Chromosome)):
            for col2 in range(col1+1,len(self.Chromosome)):
                row1 = self.Chromosome[col1]
                row2 = self.Chromosome[col2]
                self.fitnessValue-=(row1==row2)
                self.fitnessValue-=(col1+row1==col2+row2)
                self.fitnessValue-=(col1-row1==col2-row2)

    def mutate(self) -> None:
        NofQ:int = len(self.Chromosome)
        self.Chromosome[random.randint(0,NofQ-1)] = random.randint(0,NofQ-1)

class Population:
    def __init__(self, populationSize:int, NofQ:int, initialFitness:int) -> None:
        chromosome:list[int] = [random.randint(0,NofQ-1) for _ in range(NofQ)]
        self.members:list[Element] = [ Element(chromosome,initialFitness) for _ in range(populationSize)]

    def select(self, fun) -> None:
        self.members = self.members[:fun(self.members)]

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
    def __init__(self, initialPopulationSize:int, maxPopulationSize:int, maxCrossoverLimit:int, crossoverPoint:int, initialFitness:int) -> None:
        self.InitialPopulationSize:int = initialPopulationSize
        self.MaxPopulationSize:int = maxPopulationSize
        self.SelectionFunction = lambda x: len(x)//2
        self.MaxCrossoverLimit:int = maxCrossoverLimit
        self.CrossoverPoint:int = crossoverPoint
        self.InitialFitness:int = initialFitness
    
    def run(self,generationLimit:int, bestValue:int, numberOfQueens:int) -> None:
        Generation:int = 0
        population:Population = Population(self.InitialPopulationSize,numberOfQueens,self.InitialFitness)
        population.fitness()
        while Generation<generationLimit:
            Generation+=1
            print(f"Generation No:{Generation}")

            population.select(self.SelectionFunction)
            population.crossover(self.MaxPopulationSize,self.MaxCrossoverLimit,self.CrossoverPoint)
            population.mutate()
            population.fitness()
            if bestValue==population.bestValues(1)[0].fitnessValue: break

        print(population.bestValues(1)[0].Chromosome)
        showBoard(population.bestValues(1)[0].Chromosome)

# spatial function to print board
def showBoard(chromosome:list[int]):
    N = len(chromosome)
    board = [[" "]*N for _ in range(N)]
    for col,row in enumerate(chromosome): board[row][col] = 'Q'
    for row in board:
        print(row)

if __name__=="__main__":
    ncr = lambda n: n*(n-1)>>1
    NumberOfQueens = 8
    Algorithm:AlgorithmRunner = AlgorithmRunner(
        initialPopulationSize=80,
        maxPopulationSize=500,
        maxCrossoverLimit=10,
        crossoverPoint=2,
        initialFitness= -ncr(NumberOfQueens)
    )

    Algorithm.run(generationLimit=10,bestValue=0,numberOfQueens=NumberOfQueens)