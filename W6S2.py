"""
Christian Guiang
Week 6, Session 2
July 9, 2026

Remember to use Word Wrap!
"""

import random

### DO THIS PROBLEM FIRST! ###

"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
"""

def sosd(n):
    sumOfSquaredDigits = 0
    while n != 0:
        sumOfSquaredDigits += (n%10)**2
        n = n // 10
    return sumOfSquaredDigits

def isHappy(n, displaySteps = False):
    """
    :type n: int
    :rtype: bool

    (U)
    Given a positive int "n", repeatedly square its digits and sum them together, then check if that 
    sum = 1, then return True. Otherwise, repeat the process until the sum eventually equals 1 or a 
    cycle is found.

    (P)
    Start with a list "foundSums" that starts with the first sum of squared digits from n.
    Then, while the calculated sum "sum" != 1:
        - Recalculate the sum of squared digits from sum's digits.
        - If the new sum is in foundSums, a cycle is found; return False.
        - Otherwise:
            - Add the current sum to foundSums.
            - Set sum to that new value.
        If the loop ends, return True.
    """

    foundSums = []
    currentSum = sosd(n)
    while currentSum != 1:
        newSum = sosd(currentSum)
        if displaySteps:
            print(f"current sum = {currentSum}, new sum = {newSum}")
        if newSum in foundSums:
            return False
        else:
            foundSums.append(newSum)
            currentSum = newSum
    return True

# happyTests = [19, 2, 100, random.randint(1, 100), random.randint(1, 100000), random.randint(1, 999999)]
# for num in happyTests:
#     print(f"Is {num} a happy number?: {isHappy(num, True)}\n")
# print("\n\n\n")
# dragon = random.randint(1, 999999)
# while not isHappy(dragon):
#     print(f"Is {dragon} a happy number?: {isHappy(dragon)}\n")
#     dragon = random.randint(1, 999999)
# print(f"{dragon} is a happy number! Yay!")
# print("all done!")



### SET 1 ###

# The Node class setup we'll use for all these problems.
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# A print function used for testing.
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# 1. Wild Goose Chase
def is_circular(clues):
    """
    You're a detective and have been given an anonymous tip on your latest case, but something about it seems fishy - you suspect the clue might be a red herring meant to send you around in circles. Write a function is_circular() that accepts the head of a singly linked list clues and returns True if the tail of the linked list points at the head of the linked list. Otherwise, return False.

    (U)
    Given the head of a singly linked list, check if the linked list is circular, or if the tail points to the head.

    Input: head (Node)
    Output: True if the linked list is circular, False otherwise

    (M)
    The first thought may be to use a slow-fast pointer set up, but that's actually more complex than is needed. This problem is only asking to check if a specific link exists, i.e., a link between the head and some node that would be the tail, so the solution only needs to check if that one link exists. In other words, this is just a linked list traversal problem.

    (P)
    Since we're only checking for one link that's between the head and tail, we can just go through the list checking if there's some node that links back to the head (node.next = head, given "head" as a parameter). 
    
    So, use a while loop with a condition of (currentNode != None), where "currentNode" starts at the head. Then:
        Check if currentNode.next == head. If so, return True.
        Set currentNode to currentNode.next to progress.
    If the loop ends, the linked list is gone through, and is not circular. Return False.

    Time complexity: O(n), since this only goes through the list once.
    Space complexity: O(1), since only one node is stored and checked at a time.
    """
    currentNode = clues
    while currentNode:
        if currentNode.next == clues:
            return True
        currentNode = currentNode.next
    return False

# Should return True
# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue1

# print(is_circular(clue1))

# 2. Breaking the Cycle
def collect_false_evidence(evidence):
    """
    All the clues that lead us in circles are false evidence we need to purge! Given the head of a linked list evidence, clean up the evidence list by identifying any false clues. Write a function collect_false_evidence() that returns an array containing all values that are part of any cycle in evidence. Return the values in any order.

    (U)
    Given the head of a singly linked list, check if it has a cycle created by a node pointing to some earlier node in the list. If so, return a list of all the values in the cycle, in any order.

    Input: head (Node)
    Output: True if the linked list has a cycle, False otherwise

    (M)
    This also doesn't need a slow-fast pointer method because it follows the same principle as is_circular(); it just checks other nodes than the head for a cycle. So, this is a linked list traversal problem that also needs a way to track visited nodes.

    (P)
    In order to track visited nodes, use a list "foundNodes". Any nodes that we come across will have to be checked against the nodes in this to find cycles.

    So, let's use a while loop with condition currentNode != None:
        Check if currentNode is in foundNodes.
            If so, a cycle has been found.
                Begin a for loop running from currentNode to the end of foundNodes, say with n in foundNodes[currentNode.index : end].
                    Append each node n's value to a list "ret".
                Return ret.
            Otherwise, append currentNode to foundNodes. This keeps the nodes' order from the linked list, and makes it possible to easily remove all nodes that follow the return point of a cycle.
        Set currentNode to its next node to progress.
    If the while loop ends, there were no cycles. Return an empty list.

    Time complexity: O(2n) -> O(n), since the list is traversed at most twice fully; once for finding cycles, and once for getting values from a cycle with all nodes in it.
    Space complexity: O(2n) -> O(n), since two arrays that are at worst length n are made. This happens if the list is circular.
    """
    foundNodes = []
    currentNode = evidence
    while currentNode:
        if currentNode in foundNodes:
            startIndex = foundNodes.index(currentNode)
            ret = []
            for n in foundNodes[startIndex:]:
                ret.append(n.value)
            return ret
        foundNodes.append(currentNode)
        currentNode = currentNode.next
    return []

# clue1 = Node("Unmarked sedan seen near the crime scene")
# clue2 = Node("The stolen goods are at an abandoned warehouse")
# clue3 = Node("The mayor is accepting bribes")
# clue4 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue4
# clue4.next = clue2

# clue5 = Node("A masked figure was seen fleeing the scene")
# clue6 = Node("Footprints lead to the nearby woods")
# clue7 = Node("A broken window was found at the back")
# clue5.next = clue6
# clue6.next = clue7

# print(collect_false_evidence(clue1))
# print(collect_false_evidence(clue5))

# 3. Prioritizing Suspects
def stitch_nodes(node_list: list[Node]):
    """
    This is a helper function that takes a list of Nodes and creates a new linked list out of them, preserving their initial order and overwriting any previous links they might have had. Returns the head of the new linked list.
    """
    if len(node_list) < 1:
        return None
    else:
        head = node_list[0]
        current = head
        for n in node_list[1:]:
            current.next = n
            current = current.next
        # Be sure to overwrite the last node's link to None, or you might get cycles later on.
        current.next = None
        return head


def partition(suspect_ratings, threshold):
    """
    You've identified a list of suspect, but time is limited and you won't be able to question all of them today. Write a function partition() to help prioritize the order in which you question suspects. Given the head of a linked list of integers suspect_ratings, where each integer represents the suspiciousness of the a given suspect and a value threshold, partition the linked list such that all nodes with values greater than threshold come before nodes with values less than or equal to threshold.

    Return the head of the partitioned list.

    (U)
    Given the head of a linked list of integers and a value threshold, partition the list such that all nodes with values greater than the threshold come before all nodes with values less than or equal to the threshold.

    Input: head (Node)
    Output: Head of the partitioned list (Node)

    (M)
    This is a linked list traversal problem that also needs a way to organize nodes based on whether or they're > threshold or not. So, using buckets could also be helpful here.

    (P)
    Let's create two buckets: one for all nodes with values > the threshold, and one for all nodes with values <= the threshold. Call these "greater" and "lesser".

    Using a while loop to traverse the linked list:
        If currentNode.value > threshold, append it to greater.
        Otherwise, append it to lesser.
    Then, create two linked lists to hold the nodes in either bucket; call these greaterList and lesserList. Link the tail of greaterList to the head of lesserList, then return the head of greaterList. The order can be reversed if the nodes with lesser values (lesser priority) are wanted first instead.

    Time complexity: O(2n) -> O(n) since the whole list needs to be traversed first, plus two traversals for the sublists whose lengths together add up to n.
    Space complexity: O(2n) -> O(n) since two linked lists are being made. They have a combined length of n, though, so this maybe could be O(n) right away?
    """
    greater = []
    lesser = []
    current = suspect_ratings
    # Sort into buckets first.
    while current:
        if current.value > threshold:
            greater.append(current)
        else:
            lesser.append(current)
        current = current.next
    # Then, create separate linked lists of each bucket's nodes.
    greaterList = stitch_nodes(greater)
    lesserList = stitch_nodes(lesser)
    # Finally, link the tail of greaterList to the head of lesserList.
    tail = greaterList
    while tail.next:
        tail = tail.next
    tail.next = lesserList
    return greaterList

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))