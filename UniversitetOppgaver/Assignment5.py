#Oppgave 1.

""" 
Et fullt binært tre er et tre der alle noder har to children. Bortsett fra leavsene.
Alle trærene i oppgaven er innenfor denne definisjonen. (d)
"""

#Oppgave 2.

"""
Til slutt vil funksjonen make_tree() printe en liste av lister som reprenenterer treet.
"""

def binary_tree(r):
    return [r, [], []]

def insert_left_child(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch,[], []])
    return root

def insert_right_child(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch,[], []])
    return root


def make_tree():
    tree = binary_tree(1)
    insert_left_child(tree,2)
    insert_right_child(tree,3)
    insert_left_child(tree[1], 4)
    insert_left_child(tree[2], 5)
    insert_right_child(tree[2], 6)
    print (tree)

make_tree()


#Oppgave 3

"""
I denne oppgaven printer vi ut nodene fra graph klassen vår basert på deres naboer.
eks.
printer fra node 'a':

a -> [->'b'<-, 'c'] -> printer a
b -> [->'c'<-, 'd'] -> printer b
c -> [->'e'<-]      -> printer c
e -> [->'f'<-]      -> printer e
osv.
"""

class Graph:
    graph = dict()
    searched = []
    def add_edge(self, node, neighbour):
        if node not in self.graph: 
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)
    def depth_first_search(self, node):
        if node not in self.searched:
            print("[", node, end=" ],")
            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_first_search(neighbour)


    def print_graph(self):
        print(self.graph)


def build_my_graph2():
    my_graph = Graph()
    my_graph.add_edge('a', 'b')
    my_graph.add_edge('a', 'c')
    my_graph.add_edge('b', 'c')
    my_graph.add_edge('b', 'd')
    my_graph.add_edge('c', 'e')
    my_graph.add_edge('d', 'e')
    my_graph.add_edge('d', 'g')
    my_graph.add_edge('d', 'h')
    my_graph.add_edge('e', 'f')
    my_graph.add_edge('f', 'c')
    return my_graph

my_graph = build_my_graph2()
my_graph.print_graph()
print("\nruns Depth First Search (DFS) algorithm starting from node ‘a’ and prints all the visited nodes:")
my_graph.depth_first_search("a")

#Oppgave 4.

"""
two new methods in this
class that are described in the assignment
"""

class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        if self.value:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None
    # Sjekker om noden er tom:
    def is_empty(self):
        return self.value is None
    # Legger til noder på høyre eller venstre side basert på størrelsen
    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        elif value < self.value:
            self.left_child.insert(value)
        elif value > self.value:
            self.right_child.insert(value)
    def in_order(self):
        if self.is_empty():
            return []
        else:
            return self.left_child.in_order() + [self.value] + self.right_child.in_order()
    def compute_sum(self):
        sum = 0
        for i in self.in_order():
            sum += i
        return sum
    def compute_count(self):
        return len(self.in_order())
        
my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)
print('\n\nsum:', my_tree.compute_sum())
print('number of nodes:', my_tree.compute_count())