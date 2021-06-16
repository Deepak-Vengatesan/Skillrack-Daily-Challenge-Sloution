class City:
    __totalPopulation = 0

    def __init__(self,name,population):
        self.name = name 
        self.population = population 
        City.__totalPopulation += self.population 

    def __str__(self):
        return f"{self.name}:{self.population}"


N = int(input())
cities = []
for ctr in range(N):
    name, population = input().split() 
    cities.append(City(name, int(population)))
print(City._City__totalPopulation)
for city in cities:
    print(city)


'''

3
kktcity 19000
urcity 81000
mccity 21000

'''