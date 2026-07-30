### Base classes, just let these be ###
# Binary Tree node
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def binary_search_first(nums, target):
    l = 0
    r = len(nums) - 1
    m = (r + l) // 2
    while l <= r:
        m = (l + r) // 2
        # print(f"l = {l}, r = {r}, m = {m}")
        if target == nums[m]:
            # Check the next index to the left for duplicates.
            # print("middle searched")
            if m != 0:
                if target == nums[m-1]:
                    r = m - 1
                    m = (r + l) // 2
                else:
                    return m
            else:
                return m
        elif target < nums[m]:
            # print("right discarded")
            r = m - 1
        else:
            # print("left discarded")
            l = m + 1
        
    return -1

def valid_brackets(brickabrack):
    """
    Given an array of bracket strings "brickabrack", return an array of corresponding "YES" or "NO" strings denoting if the bracket strings are valid or not.
    Bracket strings are composed of characters "()", "[]", and "{}".

    I'm using switch statements, because they SHOULD work. Looking at you, HackerRank.
    """
    ret = []
    for s in brickabrack:
        # This needs a flag for errant closing brackets, since they wouldn't be caught otherwise.
        noExtras = True
        openers = []
        # This should iterate over every char in s...
        for b in s:
            match b:
                # Are you supposed to NOT use break? Yeah, you don't use break...
                case '(':
                    openers.append(b)
                    # break
                case '[':
                    openers.append(b)
                case '{':
                    openers.append(b)
                case ')':
                    # If any closer appears when openers is empty, raise a flag that marks this string as invalid.
                    # Also, remember that you can't use " str == "" " or "str is None" to check if a string is empty. Use the length instead, and check if it's 0 or not.
                    if len(openers) < 1:
                        noExtras = False
                    if openers and openers[-1] == '(':
                        openers.pop()
                case ']':
                    if len(openers) < 1:
                        noExtras = False
                    if openers and openers[-1] == '[':
                        openers.pop()
                case '}':
                    if len(openers) < 1:
                        noExtras = False
                    if openers and openers[-1] == '{':
                        openers.pop()
                case _:
                    print("whoa, invalid character!")
        print(f"openers = {openers}, noExtras = {noExtras}")
        if openers or not noExtras:
            ret.append("NO")
        else:
            ret.append("YES")
    return ret
            



if __name__ == "__main__":
    uNums = [1,2,3,4,5,6,7,8,9,10]
    dNums = [1,2,3,3,3,4,5]
    nNums = [0,0,0,0,0]
    target = 3

    print("GO!")
    print(f"First instance of {target} in {uNums} is at index {binary_search_first(uNums, target)}")
    print(f"First instance of {target} in {dNums} is at index {binary_search_first(dNums, target)}")
    print(f"First instance of {target} in {nNums} is at index {binary_search_first(nNums, target)}")
    

    bracks = ["()()()()", "([{}{}]([]))", "(", "{}}{{}}{}"]
    print(valid_brackets(bracks))
    print("GAME!")