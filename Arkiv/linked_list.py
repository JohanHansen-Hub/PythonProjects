
# En node er som en infomrasjonspakke som inneholder en verdi, og en pekeverdi for neste verdi i listen.
class Node:
    #Vi lager en metode som får en verdi og en "pointer"
    def __init__(self, data, next=None):
        self.data = data
        self.next_node = next

class linkedList:
    def __init__(self, head=None):
        self.head = head
    # Metode for å motta nye verdier til listen:
    def add(self, data):
        # Oppretter node:
        node = Node(data)
        # Dersom listen ikke har noen hode vil denne noden bli listens hode
        if self.head is None:
            self.head = node
            return
        # Vi starter fra hodet og jobber oss nedover listen for å plassere noden:
        this_node = self.head
        while True:
            if this_node.next_node is None:
                this_node.next_node = node
                break
            this_node = this_node.next_node
    # Printer ut alle verdier i listen
    def printList(self):
        this_node = self.head
        while this_node is not None:
            print (this_node.data, "->", end=" ")
            this_node = this_node.next_node
        print ("None")
    # Tester om listen er tom eller ikke
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    # Fjerner element fra listen
    def remove(self, data):
        # Sjekker om hodet har en verdi lik verdien vi ønsker slettet
        if self.head.data == data:
            self.head = self.head.next_node
        this_node = self.head
        # Itererer gjennom listen for å lete etter andre verdier lik data
        while True:
            if this_node.next_node is None:
                break
            # Dersom vi finner en verdi som skal slettes endrer vi pointen til den noden som kommer etter den slettede noden:
            if this_node.next_node.data == data:
                this_node.next_node = this_node.next_node.next_node
            this_node = this_node.next_node
    # Printer størrelsen til listen
    def size(self):
        size = 0
        if self.head.data is not None:
            size += 1
        this_node = self.head
        while True:
            if this_node.next_node is None:
                print("Size of list: ", size)
                break
            size += 1
            this_node = this_node.next_node
    # Fjerner siste element i listen
    def pop(self):
        this_node = self.head
        prev = None
        while True:
            if this_node.next_node is None:
                prev.next_node = None
                break
            prev = this_node
            this_node = this_node.next_node
    # Pusher element foran i listen:
    def push(self, data):
        node = Node(data)
        node.next_node = self.head
        self.head = node



linked_list = linkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(5)
linked_list.push(9)
linked_list.remove(2)
linked_list.printList()
linked_list.size()
