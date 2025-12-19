import random

class Cell:
    def __init__(self, chromosome:list, fitness:float) -> None:
        self.chromosome:list = chromosome
        self.fitness:float = fitness
    
    def getFit(self) -> None:
        pass

    def mutate(self) -> None:
        pass

class Population:
    def __init__(self, N:int) -> None:
        self.population:list[Cell] = [Cell([],0) for _ in range(N)]
        self.newGeneration:list[Cell] = []
        
    def select(self, selType = "random") -> tuple[Cell,Cell] | None:
        ln = len(self.population)
        # random
        if selType=="random":
            return self.population[random.randint(0,ln-1)], self.population[random.randint(0,ln-1)]
        elif selType=="ranked":
            return self.population[len(self.newGeneration)+1], self.population[random.randint(0,ln-1)]
        return None

    def crossover(self, p1:Cell, p2:Cell, p:int ) -> tuple[Cell,Cell]:
        c1:Cell = Cell(p1.chromosome[:p]+p2.chromosome[p:],0)
        c2:Cell = Cell(p2.chromosome[:p]+p1.chromosome[p:],0)
        return c1,c2

    def fit(self):
        for cell in self.population: cell.getFit()

    def mutate(self):
        for cell in self.population: cell.mutate()

    def sort(self ):
        self.population.sort( reverse=True, key=lambda cell: cell.fitness)
