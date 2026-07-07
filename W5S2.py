"""
Week 5, Session 2
07/02/2026
"""

### SET 1 ###

# 1. Mutual Friends
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        pass

# 2. Linked Up
"""
A linked list is a data structure that, similar to a normal list or array, allows us to store pieces of data sequentially. The key difference is how the elements are stored in memory.

In a normal list, elements are stored in adjacent memory locations. If we know the location of the first element, we can easily access any other element in the list.

In a linked list, individual elements, called nodes, are not stored in sequential memory locations. Instead, each node stores a reference or pointer to the next node in the list, allowing us to traverse the list.

Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> isabelle.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints the values of the list has also been provided for testing purposes.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# Linking the nodes...
def link_nodes(*args):
    for node in range(len(args) - 1):
        pass


# 3. Daily Tasks
"""
Imagine a linked list used as a daily task list where each node represents a task. Write a function add_task() that takes in the head of a linked list and adds a new node to the front of the task list.

The function should insert a new Node object with the value task as the new head of the linked list and return the new node.

Note: The "head" of a linked list is the first element in the linked list. It is equivalent to lst[0] of a normal list.
"""
def add_first(head, task):
    pass

# 4. Halve List
"""
Write a function halve_list() that accepts the head of a linked list whose values are integers and divides each value by two (can include decimals). Return the head of the modified list.

(U)
Starting from the head of a linked list, iterate through the linked list halving every value.
    Input: head (Node)
    Output: head (Node)

(M)
Linked List traversal

(P)
With currentNode = head, while currentNode.next != None, currentNode.value  /= 2.

Time complexity: O(n)
Space complexity: O(1)
"""
def halve_list(head):
    currentNode = head
    while currentNode != None:
        currentNode.value = float(currentNode.value / 2)
        currentNode = currentNode.next
    return head

node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))

# 5. Remove Last
"""
Write a function delete_tail() that accepts the head of a linked list and removes the last node in the list. Return the head of the modified list.

Note: The "tail" of a list is the last element in the linked list. It is equivalent to lst[-1] in a normal list.
"""
def delete_tail(head):
    pass

butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))

# 6. Find Minimum in Linked List
"""
Write a function find_min() that takes in the head of a linked list and returns the minimum value in the linked list. You can assume the linked list will contain only numeric values.


"""
head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
print(find_min(head2))
