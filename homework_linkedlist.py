class Node:
    def __init__(self, content):
        self.content = content
        self.next = None


def count_letters_to_nodes(sentence):
    words = sentence.split()

    head = None
    current = None

    for word in words:
        new_node = Node(len(word))

        if head is None:
            head = new_node
            current = new_node
        else:
            current.next = new_node
            current = new_node

    return head


def print_list(start):
    q = start
    while q is not None:
        print(q.content)
        print("----->", q.next)
        print("======")
        q = q.next


sentence = input("Enter sentence: ")
linked_list = count_letters_to_nodes(sentence)

print("\nLinked List Output:")
print_list(linked_list)