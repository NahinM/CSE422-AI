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
    def __init__(self, data:dict) -> None:
        self.data:dict = data
        self.population:list[Cell] = [data["chromosome_definition"]() for _ in range(self.data["population_size"])]
        self.newGeneration:list[Cell] = list()
        
    def select(self) -> tuple[Cell,Cell]:
        ln = len(self.population)
        if self.data["selection_type"]=="random":
            return self.population[random.randint(0,ln-1)], self.population[random.randint(0,ln-1)]
        if self.data["selection_type"]!="ranked": raise Exception(f"the {self.data['selection_type']} selection type is not available")
        return self.population[len(self.newGeneration)+1], self.population[random.randint(0,ln-1)]
        
    def crossover(self, p1:Cell, p2:Cell ) -> tuple[Cell,Cell]:
        p:int = self.data["crossover_point"]
        c1:Cell = Cell(p1.chromosome[:p]+p2.chromosome[p:],0)
        c2:Cell = Cell(p2.chromosome[:p]+p1.chromosome[p:],0)
        return c1,c2

    def fit(self):
        for cell in self.population: cell.getFit()
        self.sort()

    def mutate(self):
        for cell in self.population: cell.mutate()

    def sort(self ):
        self.population.sort( reverse=True, key=lambda cell: cell.fitness)
    
    def put_in_new_gen(self, c1:Cell, c2:Cell ) -> None:
        if len(self.population)-len(self.newGeneration)==1:
            self.newGeneration.append(c1) if random.randint(0,1)==1 else self.newGeneration.append(c2)
            return
        self.newGeneration.append(c1)
        self.newGeneration.append(c2)
    
    def generate_newGen(self):
        elits = self.data["elits"]
        while len(self.newGeneration)<len(self.population):
            if elits!=0:
                elits-=1
                self.newGeneration.append(Cell(self.population[0].chromosome.copy(),100))
                continue
            p1,p2 = self.select()
            c1,c2 = self.crossover(p1,p2)
            self.put_in_new_gen(c1,c2)
        self.population = self.newGeneration
        self.newGeneration = list()

#Selection Type
Random_,Ranked_ = "random","ranked"
data = {
    "gn":500,
    "queens": 8,
    "selection_type": Ranked_,
    "crossover_point": 5,
    "population_size": 2000,
    "elits":10,
    "chromosome_definition": lambda n : Cell([],100)
}
data["population"] = Population(data)

# running genetic algo
data["population"].fit()
best:Cell = data["population"].population[0]
for G in range(1,data["gn"]+1):
    print(f"Generation:{G}")
    data["population"].generate_newGen()
    data["population"].mutate()
    data["population"].fit()

    best = data["population"].population[0]
    if best.fitness == 0: break

print(best.chromosome)