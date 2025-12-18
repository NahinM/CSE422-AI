import random

class Cell:
    def __init__(self, chromosome:list, fitness:float) -> None:
        self.chromosome = chromosome
        self.fitness = fitness
    
    def getFit(self) -> None:
        pass

    def mutate(self) -> None:
        pass

def select( Population:list[Cell], newGeneration:list[Cell] , selType = "random") -> tuple[Cell,Cell] | None:
    ln = len(Population)
    # random
    if selType=="random":
        return Population[random.randint(0,ln-1)], Population[random.randint(0,ln-1)]
    elif selType=="ranked":
        return Population[len(newGeneration)+1], Population[random.randint(0,ln-1)]
    return None

def crossover( p1:Cell, p2:Cell ) -> tuple[Cell,Cell]:
    p = 2
    c1:Cell = Cell(p1.chromosome[:p]+p2.chromosome[p:],0)
    c2:Cell = Cell(p2.chromosome[:p]+p1.chromosome[p:],0)
    return c1,c2