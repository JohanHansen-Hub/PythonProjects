# Oppgave 1

"""
Korrekt svar på denne oppgaven er a), ettersom pre-order traversal skjer gjennom følgende steg:
1. besøk node
2. Travaser venstre
3. Travaser høyre
"""
# Oppgave 2
"""
Kilde for inspirasjon: https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
"""
from itertools import combinations

class QuizGift:
    question_values = {}
    def __init__(self, questions):
        self.question_list = []
        for k,v in questions.items():
            self.question_values[k] = {'points':v[0], 'time':v[1]}
            self.question_list.append({k:{'points':v[0], 'time':v[1]}})


    def find_sum_points_time(self, combination_list):
        sum_points = 0
        sum_time = 0
        for item in combination_list:
            for k, v in item.items():
                verdi = v['points']
                tid = v['time']
                sum_points += verdi
                sum_time += tid
        return sum_points, sum_time
    

    def find_gift(self, points):
        if points > 750:
            return "Laptop"
        elif points >= 250:
            return "Smartphone"
        else:
            return "Watch"

    # Dynamisk programmering, cacher hver kombinasjon til minnet for så å finne den kombinasjonen som optimaliserer maksimerings problemet:
    def compute_result(self, max_time):
        memorized_combinations= []
        under_max_combi= []
        # Kilde: https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
        for i in range(1, len(self.question_list)):
            liste = [list(x) for x in combinations(self.question_list, i)]
            for e in liste:
                memorized_combinations.append(e)
        for combi in memorized_combinations:
            sum_points, sum_time = self.find_sum_points_time(combi)
            if sum_time <= max_time:
                under_max_combi.append({sum_points:combi})
        sorted_combi = [i for i in sorted(under_max_combi, key=lambda e: list(e.keys())[0], reverse=True)]
        self.result = sorted_combi
            #for e in range(len(self.question_values)):
    

    def print_result(self):
        print("\nOppgave 2:\n\nResult: \n")
        for the_list in self.result[0].values():
            for i in the_list:
                for k, v in i.items():
                    print(k, "  gives points: "+ str(v['points']),"  takes time: "+ str(v['time'])+" minutes")
            sum_points, sum_time = self.find_sum_points_time(the_list)
            print("\nTotal points: "+str(sum_points)+"\nTotal time: "+str(sum_time)+" minutes")
            print("\nThe gift that she will receive: "+ self.find_gift(sum_points)+"\n")


questions = {'Question 1': [120, 15], 'Question 2': [200, 20], 'Question 3': [150, 40], 'Question 4': [350, 50], 'Question 5': [100, 20], 'Question 6': [90, 10]}
my_quiz = QuizGift(questions)
my_quiz.compute_result(max_time=100)
my_quiz.print_result()

# Oppgave 3.
from math import sqrt
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def compute_area(self):
        pass

class Square(Shape):
    def __init__(self, s):
        self.s = s
    def compute_area(self):
        print(self.s*self.s)

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def compute_area(self):
        print(3.14*self.r*2)
class Triangle(Shape):  
    def __init__(self,s1,s2,s3):
              self.a = s1
              self.b = s2
              self.c = s3
              self.s = (s1+s2+s3)/2
    def compute_area(self):
        a = self.a
        b = self.b
        c = self.c
        s = self.s
        print(sqrt(s*(s-a)*(s-b)*(s-c)))

my_square = Square(2)
my_circle = Circle(2)
my_triangle = Triangle(5, 4, 3)
print('Oppgave 2:\n\nArea of square:', end=' ')
my_square.compute_area()
print('Area of circle:', end=' ')
my_circle.compute_area()
print('Area of triangle:', end=' ')
my_triangle.compute_area()


# Oppgave 4.

class House():
    count = 0
    def __init__(self, owner, condition, price):
        self.owner = owner
        self.condition = condition
        self.price = price
        self.cost = 0
        self.sold = False
        self.count += 1
    
    def sell(self, new_owner):
        self.sold = True
        profit = self.price-self.cost
        print("{owner} sold the house with a {profit} $ profit!".format(owner=self.owner, profit=profit))
        self.owner = new_owner
    def change_price(self, new_price):
        if self.sold == True:
            print("House has been sold!")
        else:
            self.price = new_price

    def renovate(self, expense, new_condition):
        self.cost = self.cost + expense
        self.condition = new_condition
        print("\n\nHouse renovated!")
        
    def print_info(self):
        print("\n\nHouse information:\n")
        print("Owner: "+self.owner)
        print("Condition: "+self.condition)
        print("Price: "+str(self.price)+" $\n")

house1 = House("John", "Good", 100000)
house2 = House("Sara", "Very good", 250000)

house1.renovate(20000, "Very good")
house1.change_price(150000)
house1.sell("Bob")

house1.print_info()
house2.print_info()
