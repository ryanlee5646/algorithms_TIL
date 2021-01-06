import itertools
data = [1,2,3]
combi = list(itertools.combinations(data,3))
permu = list(itertools.permutations(data,3))
part = []
for i in range(len(data)+1):
    pa = list(itertools.combinations(data,i))
    for j in range(len(pa)):
        part.append([j])
print(combi)
print(permu)
print(part)