
#Number of non-negative int solutions of a+b+c=n

def findNoNNegative(n):
    integers = [i for i in range(0, n + 1)]
    antall_sett = 0
    for i in integers:
        for j in integers:
            for k in integers:
                if i + j + k == n:
                    antall_sett += 1
    return antall_sett

print(findNoNNegative(3))