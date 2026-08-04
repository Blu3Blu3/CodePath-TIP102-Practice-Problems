"""
You know who <3
Started: 7/30/2026
Finished: -----
Validated: -----
Last updated: 7/30/2026

This is a collection of different ways to traverse a binary tree, ranging from the standard preorder/inorder/postorder to more esoteric ways, like zigzag. I initially made this to test an implementation of the zigzag traversal after trying it out in a CodePath lecture, but this whole file works well as a testing ground / sandbox for all the other binary tree traversals too.

Ideally, each traversal has a recursive version and an iterative version, with a way to select between them.

TODO: Write driver code for a basic UI in the command line. Namely, have a menu to choose a function from what's available in a given file or list, and a way to add/edit/choose trees to work over.
TODO: When that's done, update the driver code to work with a number of different variable types, and a way to save/load to and from a file. Maybe that's a way to test saving and loading for games too? Probably. Give it a shot!
"""

from collections import deque
from typing import List

# Class and helpers, don't touch
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

######################################

# NOTE: The implementation towards the end gets pretty hacky since I couldn't think of another, better way to build a list of lists recursively, thus necessitating parsing some super-nested lists.
def breadth_first_traversal_recursive(root):
    """
    Given the root "root" of a binary tree, return the nodes traversed in breadth-first order (level by level starting from the root, left to right) as a list of lists ([[root], [level 2 nodes], [level 3 nodes], ...])

    (Plan)
    First, check if the root is null. If so, return []. Otherwise, start the traversal with a helper function "traverse(nodes)" that takes in a queue of nodes as a parameter and returns a list of lists as described above.

    In traverse(nodes), have a new queue "nextLevel" that will hold the children of each node in "nodes", which are appended to nextLevel as their parents are popped from nodes. In other words, while there are nodes in the queue nodes, append any non-null children to nextLevel, and add the current node's value to a new list "thisLevel" while removing the current node from the queue (nodes.popleft). Return [thisLevel, traverse(nextLevel)].

    Finally, return traverse(root) in the main function.

    NOTE: The queues here can actually be replaced with lists if the loop is adjusted a bit. If using lists, the while loop or any loop will just have to list over each index from 0 to the end, instead of having nodes be popped.
    """
    # Null check
    if root is None:
        return []

    def traverse_level(nodes: List[TreeNode]):
        """
        Given all nodes on a level of a binary tree, recursively return a list of each following level's node values, traversed from left to right. If given the root of a binary tree in a list, this will return a list of each level's node values in the list in accordance with BFS.
        """
        # nextLevel is a list for TreeNodes. thisLevelVals is a list for int values from each node in this level.
        nextLevel = []
        thisLevelVals = []
        for node in nodes:
            # Null check first; if current node is null, move to the next.
            if node is None:
                continue

            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            thisLevelVals.append(node.val)

        # Remember to check if this is the last level.
        if len(nextLevel) < 1:
            return thisLevelVals
        thisLevelVals.append(traverse_level(nextLevel))
        return thisLevelVals

    # After getting the traversal, the results need to be parsed
    traversal = traverse_level([root])
    currentList = traversal[1]
    newLevel = []
    ret = [[traversal[0]]]
    while currentList:
        if type(currentList[0]) == type(1):
            newLevel.append(currentList[0])
            currentList.pop(0)
        # If the next element to pop from the current list (which is essentially a queue now) isn't an int (i.e., it's a list), set the current list to the list in the first index
        else:
            currentList = currentList[0]
            ret.append(newLevel)
            newLevel = []
    ret.append(newLevel)
    return ret

# NOTE: So much cleaner than the recursive, omg...
def breadth_first_traversal_iterative(root):
    """
    Given the root "root" of a binary tree, return a list of lists, each containing the nodes on each level of the tree, starting from the root level.

    Same as the recursive method, but without the need for a helper function or any parsing. This is doable with one or two queues and a while loop.

    Start by having two queues "thisLevel" and "nextLevel", and an empty list "newLevel".
    If root is null, return [].
    Otherwise, append root to thisLevel.
    While thisLevel has nodes queued:
        Pop the next element in thisLevel (call this "current"), and append its value to newLevel
        If current has any children, append them to nextLevel. Left goes first if it's there.
        Check if thisLevel is empty, signaling that the current level's nodes have all been traversed.
            If so:
                Append newLevel to a return list "levels", then set newLevel to a new, empty list.
                Set thisLevel to nextLevel, queueing up all the next level's nodes.
                Clear nextLevel.
    Return levels.
    """
    if root is None:
        return []
    newLevel, levels = [], []
    thisLevel, nextLevel = deque(), deque()
    thisLevel.append(root)
    while len(thisLevel) > 0:
        current = thisLevel.popleft()
        newLevel.append(current.val)
        if current.left:
            nextLevel.append(current.left)
        if current.right:
            nextLevel.append(current.right)

        if len(thisLevel) == 0:
            levels.append(newLevel)
            newLevel = []
            # Remember to use copies of lists or other iterables when setting other iterables to them.
            # Otherwise, you'll just use a reference of the iterable which reflects any changes to the original.
            thisLevel = nextLevel.copy()
            nextLevel.clear()
    return levels

def zigzag_easy(root):
    """
    Given the root "root" of a binary tree, return the nodes on each level when traversing in "zigzag" order, going from left to right at the root level, right to left at the second level, left to right at the third level, and so forth. 

    This is called "zigzag_easy" since we're just using BF traversal and reversing the order of every other row to get the nodes going from right to left.
    """
    levels = breadth_first_traversal_iterative(root)
    for l in range(len(levels)):
        if l % 2 == 1:
            levels[l].reverse()
    return levels

# TODO: Fix this, it's messing some things up.
def zigzag_hard(root):
    """
    Given the root "root" of a binary tree, return the nodes on each level when traversing in "zigzag" order, going from left to right at the root level, right to left at the second level, left to right at the third level, and so forth. 

    This is called "zigzag_hard" because it actually finds and traverses the nodes in each level itself, instead of relying on another BF traversal function. I mean, it's basically identical to the iterative BF traversal function with the addition of a flag for reversing a level, but...
    """
    if root is None:
        return []
    newLevel, levels = [], []
    thisLevel, nextLevel = deque(), deque()
    flip = True
    thisLevel.append(root)
    while len(thisLevel) > 0:
        current = thisLevel.popleft()
        newLevel.append(current.val)
        if flip:
            if current.left:
                nextLevel.appendleft(current.left)
            if current.right:
                nextLevel.appendleft(current.right)
        else:
            if current.left:
                nextLevel.append(current.left)
            if current.right:
                nextLevel.append(current.right)

        if len(thisLevel) == 0:
            levels.append(newLevel)
            newLevel = []
            # Remember to use copies of lists or other iterables when setting other iterables to them.
            # Otherwise, you'll just use a reference of the iterable which reflects any changes to the original.
            thisLevel = nextLevel.copy()
            nextLevel.clear()
            if flip:
                flip = False
            else:
                flip = True
    return levels
    

#############################################
if __name__ == "__main__":
    root = [3, 9, 20, None, None, 15, 7, 10, 12, 13, 14, 2, 3, 4, 5]
    tree = build_tree(root)
    print_tree(tree)
    print(f"BF recursive: {breadth_first_traversal_recursive(tree)}")
    print(f"BF iterative: {breadth_first_traversal_iterative(tree)}")
    print(f"Zigzag easy: {zigzag_easy(tree)}")
    print(f"Zigzag hard: {zigzag_hard(tree)}")
