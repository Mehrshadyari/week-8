class Node:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def add_at_start(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_after_name(self, target, new_node):
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr is not None:
            if curr.name == target:
                new_node.next = curr.next
                curr.next = new_node
                return
            curr = curr.next

    def add_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def show_all(self):
        curr = self.head
        while curr is not None:
            print(curr.name, curr.age, curr.gender)
            curr = curr.next
