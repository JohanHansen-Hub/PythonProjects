# Oppgave 1

"""
Korrekt svar på denne oppgaven er a), ettersom pre-order traversal skjer med følgende steg:
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
    def compute_points_per_time(self):
        for k,v in self.question_values.items():
            marginal_points = v['points']/v['time']
            self.question_values[k]['marginal_points'] = marginal_points
        sorted_quest = {k: v for k, v in sorted(self.question_values.items(), key=lambda e: e[1]['marginal_points'], reverse=True)}
        print(sorted_quest)

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
        print("Result: \n")
        for the_list in self.result[0].values():
            for i in the_list:
                for k, v in i.items():
                    print(k, "  gives points: "+ str(v['points']),"  takes time: "+ str(v['time'])+" minutes")
            sum_points, sum_time = self.find_sum_points_time(the_list)
            print("\nTotal points: "+str(sum_points)+"\nTotal time: "+str(sum_time)+" minutes")
            print("\nThe gift that she will receive: "+ self.find_gift(sum_points))


questions = {'Question 1': [120, 15], 'Question 2': [200, 20], 'Question 3': [150, 40], 'Question 4': [350, 50], 'Question 5': [100, 20], 'Question 6': [90, 10]}
my_quiz = QuizGift(questions)
my_quiz.compute_result(max_time=100)
my_quiz.print_result()