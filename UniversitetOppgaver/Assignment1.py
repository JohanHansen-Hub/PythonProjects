#Oppgave 1

def max_binary_search(n):
    x = n
    steps = 0
    #Vi ønsker å finne ut hvor lang tid det vil ta å komme til n = 1 ved å dele på 2
    while n > 1:
        n = n // 2
        steps +=1
    return print('Max steps used = '+str(steps) + ' FOR n = '+str(x))
max_binary_search(262144)
max_binary_search(1100373)
max_binary_search(260000)

#Oppgave 2

class School:
    def __init__(self, name = 'Sara'):
        self.student = name
    def print_hello(self):
        print('Hello!')
sara = School()
gunnar = School('Gunnar')
sara.print_hello()
print(sara.student)
print(gunnar.student)

#Oppgave 3

class Node:
    def __init__(self, data, n = None):
        self.data = data
        self.next_node = n
    def get_next(self):
        return self.next_node
    def get_data(self):
        return self.data
class LinkedList:
    #I starten er noden selve hodet til listen (altå head == None)
    def __init__(self):
        self.head = None
        self.size = 0
    #Legger til et nytt "head" der denne noden blir degradert fra nettopp denne posisjonen
    def add(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1
    def print_list(self):
        this_node = self.head
        size = self.size
        print('\nLinkedList:')
        for i in range(0, size, 1):
            print(this_node.get_data())
            this_node = this_node.get_next()

new_list = LinkedList()
new_list.add('feet')
new_list.add('body')
new_list.add('head')

new_list.print_list()
