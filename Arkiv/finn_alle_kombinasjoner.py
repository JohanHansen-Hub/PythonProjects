from itertools import combinations

tallverdier = [1,2,3,4,5,6]

for i in range(1, len(tallverdier)):
    liste = [print(list(x)) for x in combinations(tallverdier, i)]
