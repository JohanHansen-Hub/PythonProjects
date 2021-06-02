

class Graph:
    graph = dict()

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def find_cycle(self, node):
        pos_node = None
        if node in self.graph:
            pos_node = list(self.graph).index(node)
        # DFS
        # Starter fra nodes posisjon
        for e in range(pos_node, len(self.graph)):
            found = []
            #Sjekker etter en løkke i nodens naboer
            for x in list(self.graph.values())[e]:
                if self.graph.get(x) is not None:
                    # Legger sammen naboenes edger:
                    for z in self.graph.get(x):
                        found.append(z)
            # Sjekker om vi har funnet en felles node som binder nodene sammen -> vi har en løkke:
            if len(found) != len(set(found)):
                return 'Cycle found!'
        return
    def print_graph(self):
        print(self.graph)

my_graph = Graph()
my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('B', 'D')
my_graph.add_edge('D', 'E')
my_graph.add_edge('D', 'F')
my_graph.add_edge('C', 'E')
my_graph.add_edge('E', 'G')
my_graph.add_edge('F', 'H')
result = my_graph.find_cycle('A')
print(result)