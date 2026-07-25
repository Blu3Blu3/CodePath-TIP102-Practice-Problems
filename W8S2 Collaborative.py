# Week 8, Session 2
# This is from the session breakout room. Shoutouts to everyone who worked on it!
from collections import deque

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def build_tree(values):
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

# Problem 1: Monstera Madness
# def count_odd_splits(root):
#     odd_count = 0

#     def in_order_traversal(node):
#         nonlocal odd_count
#         if node is None:
#             return 0
#         in_order_traversal(node.left)
#         if node.val % 2 != 0:
#             odd_count += 1
#         in_order_traversal(node.right)

#         return odd_count
#     return in_order_traversal(root)
def count_odd_splits(root):
    if root is None:
        return 0
    if root.val %2 != 0:
        return 1 + count_odd_splits(root.left) + count_odd_splits(root.right)
    else:
        return count_odd_splits(root.left) + count_odd_splits(root.right)

# values = [2, 3, 5, 6, 7, None, 12]
# monstera = build_tree(values)

# print(count_odd_splits(monstera)) # Should return 3
# print(count_odd_splits(None)) # Should return 0

# Problem 2: Flower Finding

def find_flower_recursive(inventory, name):
    if inventory is None:
        return False
    if inventory.val == name:
        return True
    return find_flower(inventory.left, name) or find_flower(inventory.right, name)
#time: o(n)
#space complexity: 0(H)
def find_flower(inventory, name):
    if inventory is None:
        return False
    current = inventory
    while current:
        if current.val < name:
            current = current.right
        elif current.val > name:
            current = current.left
        else:
            return True
    return False

#Time complexity: O(H) - if it balance, o(logn)
#                        - if it is skew, O(n)
# Space : O(1)
"""
         Rose
        /    \\
      Lilac   Tulip                             Ebel
     /  \\      \\
  Daisy  Lily  Violet
    /
Abel
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]

garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 

# Problem 4: 

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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



def add_plant(collection, name):
    """
    Time complexity = O(H)
    Space complexity = O(H)
    """
    if collection is None:
        return TreeNode(name)
    if collection.val > name:
       collection.left = add_plant(collection.left, name)
    else:
        collection.right = add_plant(collection.right, name)
    return collection

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Snake Plant"))



class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key      # Plant rarity
        self.val = value      # Plant name
        self.left = left
        self.right = right


def sort_plants(collection):
    # if collection is None:
    #     return []
    # left = sort_plants(collection.left)
    # right = sort_plants(collection.right)
    # return  left + [(collection.val, collection.key)] + right
    result = []
    def inOrder(collection):
            if collection is None:
                return 
            inOrder(collection.left)
            result.append((collection.val, collection.key))
            inOrder(collection.right)
    return result
"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
    /
  None         None
"""

# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))

#[(1, 'Pothos'), (2, 'Spider Plant'), (3, 'Monstera'), (4, 'Hoya Motoskei'), (5, 'Witchcraft Orchid')]