# Oppgave 1

# C

#Oppgave 2

# iv

#Oppgave 3

def my_func1(inputs):
    n = len(inputs)
    result = 0
    for i in range(n):
        j = 1
        while j < n:
            result += inputs[i] * inputs[j]
            j *= 2
    return result

# O(nlog(n)) (avhenger av input lengden -> itereres eksponensielt)

def my_func2(inputs):
    n = len(inputs)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if inputs[j] > inputs[j + 1]:
                tmp = inputs[j]
                inputs[j] = inputs[j + 1]
                inputs[j + 1] = tmp

# O(n^2) (to for løkker -> eksponensielt)

# Oppgave 4.

def solve_problem(liste):
    lengde = len(liste)
    sum = 0
    for i in liste:
        sum += i
    result = sum / lengde + 1
    return result

# O(n) Avhenger av lenden til listen linjært, en ekstra verdi i listen fører til en ekstra iterasjon.

web_usage = [10.9, 50.2, 30.4, 10.0, 90.0]

res = solve_problem(web_usage)
print("solution:", res)