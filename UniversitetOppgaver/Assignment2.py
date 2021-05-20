#Oppgave 1
my_list = [1340, 1660, 1449, 1241, 1530]
def three_passes_selection_sort(list):
    for i in range(0, 3):
        min_index = i
        #Leter etter lavere verdier
        for e in range(i + 1, len(list) - 1):
            if list[e] < list[min_index]:
                min_index = e
        #Verdiene bytter index possisjon
        list[i], list[min_index] = list[min_index], list[i]
    return list
print(three_passes_selection_sort(my_list))
print("Vi ser dette samsvarer med listen gitt i d)")



#Oppgave 2
def sort_and_rem_dup(list):
    for i in range(len(list)-1):
        min_index = i
        #Leter etter lavere verdier
        for e in range(i + 1, len(list) - 1):
            if list[e] < list[min_index]: min_index = e
        # Verdiene bytter index possisjon
        list[i], list[min_index] = list[min_index], list[i]
    index = 0
    for i in list:
        try:
            while i == list[index+1]:
                del list[index+1]
        except:
            break
        index += 1
    return list
my_list = [5,4,3,2,1,2,3,4,5]
new_list = sort_and_rem_dup(my_list)
print("\n[Output]:\n"+str(new_list))



#Oppgave 3

class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

def reverse_list(list):
    # Bygger en Stack fra elementene i listen:
    stack = Stack()
    for i in list:
        stack.push(i)
    #Printer ut den reverserte listen
    new_list = []
    for i in range(len(stack.items)):
        delete = stack.pop()
        new_list.append(delete)
    print("\n[Output]:\n"+str(new_list))

my_list = [1,2,3,4,5]
reverse_list(my_list)
