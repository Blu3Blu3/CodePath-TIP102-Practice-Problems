"""
Christian Guiang
Week 8, Session 2
Started: 7/23/2026
Finished: -----
Validated: -----
Last updated: 7/25/2026
"""
from collections import deque

# Necessary classes and helper functions
class TreeNode():
    # Note that value doesn't have a default so you can add any type.
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

def build_tree(values):
    """
    Creates a binary tree of nodes holding the values in a given list. If the values are tuples in the form (k, v), they will be treated as the resulting nodes' keys and values.
    """
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1

    return root

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# Helper function demonstrations, uncomment when wanted
# root1 = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5), TreeNode(6)))
# root2 = build_tree(["Alice", "Barb", "Cassidy", "Denise", "Ellie"])
# print("Tree 1:")
# print_tree(root1)
# print("Tree 2:")
# print_tree(root2)



### SET 1 ###

# 1. Grafting Apples
"""
You are grafting different varieties of apple onto the same root tree can produce many different varieties of apples! Given the TreeNode class, create the binary tree depicted below. The text representing each node should should be used as the value.

             Trunk
          /         \\
      Mcintosh   Granny Smith
      /     \\       /     \\
    Fuji   Opal   Crab   Gala

# NOTE: For some reason Pylance still picks up single backslashes in docstrings and comments, so I doubled them up.
"""

"""
Not much to this, but let's go through it anyway without using build_tree().

The TreeNode constructor takes parameters in the order (value, left, right), and we can create new TreeNodes inside it instead of declaring and initializing them prior. We just need to be careful with the parentheses and the layout, since it's easy to miss something if we're writing all the nodes in one line. Let's start from the root.
"""
root = TreeNode("Trunk",
                TreeNode("McIntosh",
                         TreeNode("Fuji"),
                         TreeNode("Opal")
                        ), 
                TreeNode("Granny Smith",
                         TreeNode("Crab"),
                         TreeNode("Gala")
                        )
                )

# print_tree(root)

# 2. Calculating Yield
"""
You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

    Leaf nodes have an integer value.
    The root has a string value of either "+", "-", "*", or "-".

The yield of a the tree is calculated by applying the mathematical operation to the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""
def calculate_yield(root):
    """
    (U)
    Given a binary tree representing a mathematical expression as a root and its two leaf nodes in the following format, return the result of the expression.

        Each leaf node holds an integer value.
        The root node holds a string value that's an operation in ["+", "-", "*", "/"].

    Input: Binary tree, formatted as aforementioned
    Output: Result (int/float) of the expression represented by the binary tree
    Edge cases:
        - Any operator (root.val) value outside +, -, *, or / will cause 0 to be returned.
        - Mismatched leaf values will throw an error, but that's not worth fixing right now.

    (M)
    Not much binary tree traversal since we're only checking two levels, but this is binary tree traversal regardless.

    (P)
    Since the tree is just an expression written in a different way, all that needs to be done is finding the values to work with, then applying the correct operator. The values can be gotten using "root.left.val" and "root.right.val", and the operator can be gotten using "root.val". We just need to use a switch statement or so to check which operator it is.

    Time complexity: O(1), since there are only standalone checks of values rather than loops.
    Space complexity: O(1), since nothing gets stored.
    """
    match root.val:
        case "+":
            return root.left.val + root.right.val
        case "-":
            return root.left.val - root.right.val
        case "*":
            return root.left.val * root.right.val
        case "/":
            return root.left.val * root.right.val
        case _:
            # Maybe if there were other operations, this wouldn't fire as much.
            return 0

# apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# print(calculate_yield(apple_tree))

# 3 & 4. Ivy Cutting I and II
"""
(I)
You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node. If there is no right child, return only the root node value (the rightmost path in this case is just the root node).

(II)
If you implemented right_vine() iteratively in the previous problem, implement it recursively. If you implemented it recursively, implement it iteratively.
"""
def right_vine_iterative(root):
    """
    (U)
    Return a list of values in order of traversal moving from the root of a given tree to the rightmost node. If there is no right child of the root, return the root node value.

    (M)
    This is binary tree traversal, but there are options here for recursion.

    (P)
    No matter if this is done iteratively or recursively, this has to start at the root, move to its right child, append its value to a list, and then repeat until there is no right child to move to. Then, it has to return the list it made.

    Iteratively, this can be done with a while loop with some pointer "current":

    Create list "rightVine" = []
    Set current to root
    While current is not None:
        Append current.val to rightVine
        current = current.right to move to the right child
    Return rightVine

    Time complexity: O(H), where "H" is the height of the tree. It could be O(n) = O(H) in a tree with only right children.
    Space complexity: O(H), since a list is used to store the values.

    Recursively, this can be done by having a base case where the root is None, and a recursive call to the next right child if that doesn't apply.

    Check if root = None:
        If so, return an empty list [].
        Otherwise, return [root.val] + right_vine(root.right), keeping the recursion going until the base case is hit.

    Time complexity: O(H) overall.
    Space complexity: O(1)? I think? Just because there isn't a list being stored, and it's pieced together only at the end anyhow.
    """
    current = root
    rightVine = []
    while current:
        rightVine.append(current.val)
        current = current.right
    return rightVine

def right_vine_recursive(root):
    # Base case first.
    if root is None:
        return []
    else:
        return [root.val] + right_vine_recursive(root.right)

# Oooh, this is actually a really nice way to format the constructor! Let's adjust problem 1 like this!
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print("Ivy 1 is:")
# print_tree(ivy1)
# print("Ivy 2 is:")
# print_tree(ivy2)

# print("\nIterative results:")
# print(right_vine_iterative(ivy1))
# print(right_vine_iterative(ivy2))
# print("\nRecursive results:")
# print(right_vine_recursive(ivy1))
# print(right_vine_recursive(ivy2))

# 5. Count the Tree Leaves
"""
You've grown an oak tree from a tiny little acorn and it's finally sprouting leaves! Given the root of a binary tree representing your oak tree, count the number of leaf nodes in the tree. A leaf node is a node that does not have any children.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
def count_leaves(root):
    """
    (U)
    Given the root of a binary tree, return the amount of leaf nodes in it.

    (M)
    Binary tree traversal, but with a focus on the lowest level.

    (P)
    Traversal can go in any order (preorder, inorder, postorder), but maybe inorder is most helpful here. Anyhow, we need to traverse the tree to its lowest level (i.e., when a current node has no children) across every subtree, counting every node that has no children (node.left = None, node.right = None).

    Create a tracker "count" for the leaves, and set it to 0.
    Create a queue "nodesToVisit", and set it to [].
    Set a pointer "current" to the root.
    While current isn't None or nodesToVisit isn't empty:
        If current isn't None:
            Push current to the queue.
            Move to current's left child (current = current.left).
        Otherwise, check the queue:
            Pop the element next up in the queue, and set current to it (current = nodesToVisit.pop())
            Check if current is a leaf node (current.left is None, current.right is None):
                If so, increment count by 1.
            Move to current's right child (current = current.right) to check the right subtree.

    Time complexity: O(n * H), since every node needs to be visited, and at worst they're at the very bottom of the tree.
    Space complexity: O(n), since every node needs to be tracked.
    """
    count = 0
    current = root
    nextNodes = []
    while current and nextNodes:
        if current:
            nextNodes.append(current)
            current = current.left
        else:
            current = nextNodes.pop()
            if current.left is None and current.right is None:
                count += 1
            current = current.right
    return count

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(count_leaves(oak1))
print(count_leaves(oak2))



