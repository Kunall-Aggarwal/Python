class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == '__main__':

    lt = LinkedList()

    lt.push(1)
    lt.push(2)
    lt.push(3)
    lt.push(4)

    lt.printlist()
