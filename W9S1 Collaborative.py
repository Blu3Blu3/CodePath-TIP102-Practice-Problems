# Week 9, Session 1
from collections import deque

class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
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

### SET 1 ###

# Problem 1: Merging Cookie Orders
"""
Understand - Merge 2 trees together into one tree. Return the root. If both nodes overlap then sum their values. 
Match - 
Plan:
    Perform DFS to reach the bottom levels of both trees
    Start combining the values of nodes on the bottom level, storing them in new nodes appended to a stack
        If one tree has a None value in a given spot where the other has a node value, use the value of the existing node
        If both are none, don't add a node in that spot (add None)
    Repeat on the next level up, working until the root.
    Once the new root node has been created and appended to the stack, repeatedly:
        Pop the next element in the stack and append it to a new binary tree, moving left to right on each level

    Conditions:
        - If t1 has a node where t2 doesn't --> use t1's value
        - vice versa
        - If t1 and t2 both have a node in the same spot, sum them, use the sum
        - Else (both are None), use None

    root.val = order1.val + order2.val (after running checks)
    root.left = merge_orders(order1.left, order2.left)
    root.left = merge_orders(order1.left, order2.left)
Implement -

"""
def merge_orders(order1, order2):
    new_node = TreeNode(0)

    if order1 and not order2:
        new_node.val = order1.val
    elif not order1 and order2:
        new_node.val = order2.val
    elif not order1 and not order2:
        return None
    else:
        new_node.val = order1.val + order2.val

    new_node.left = merge_orders(order1.left if order1 else None, order2.left if order2 else None)
    new_node.right = merge_orders(order1.right if order1 else None, order2.right if order2 else None)
    return new_node

# Using build_tree() function included at top of page
# cookies1 = [1, 3, 2, 5]
# cookies2 = [2, 1, 3, None, 4, None, 7]
# order1 = build_tree(cookies1)
# order2 = build_tree(cookies2)

# # Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))

# Problem 2: Croquembouche

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    """
    Understand:

    Match:
    Plan:
        If the tree is empty:
    return an empty list

    Create an empty queue
    Create an empty list to store visited nodes

    Add the root into the queue

    While the queue is not empty:
        Pop the next node off the queue 
        Add the popped node to the list of visited nodes

        Add the popped node's left child to the queue
        Add the popped node's right child to the queue
    """
    if not design:
        return []
    toVisit = deque()
    visited = []

    toVisit.append(design)
    while toVisit:
        current = toVisit.popleft()
        visited.append(current.val)

        if current.left:
            toVisit.append(current.left)
        if current.right:
            toVisit.append(current.right)

    print(visited)
        
# croquembouche = Puff("Vanilla", 
#                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#                     Puff("Strawberry"))
# print_design(croquembouche)

# Problem 3: Maximum Tiers in Cake
def max_tiers_dfs(cake):
    if cake is None:
        return 0
    else:
        return 1 + max(max_tiers_dfs(cake.left), max_tiers_dfs(cake.right))

def max_tiers_bfs(cake):
    toVisit = deque()
    toVisit.append(cake)

    level = 0
    while toVisit:
        current = toVisit.popleft()
        level += 1
        for _ in range(len(queue)):
            if current.left:
                toVisit.append(current.left)
            if current.right:
                toVisit.append(current.right)

    return level
    

cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(f"DFS max tiers = {max_tiers_dfs(cake)}")
print(f"BFS max tiers = {max_tiers_bfs(cake)}")