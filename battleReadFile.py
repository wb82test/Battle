import numpy
with open("battle.txt", 'r') as f:
   l = [i.strip("\n").split() for i in f.readlines()]
x = 4
y = 4
results=(numpy.matrix(l)[:x,:y])
print(results)
print(results[1,2])

