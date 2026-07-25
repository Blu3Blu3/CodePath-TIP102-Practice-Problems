### Base classes, just let these be ###
# Binary Tree node
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):

def binary_search_first(nums, target):
    l = 0
    r = len(nums) - 1
    m = (r + l) // 2
    while l <= r:
        m = (l + r) // 2
        print(f"l = {l}, r = {r}, m = {m}")
        if target == nums[m]:
            # Check the next index to the left for duplicates.
            print("middle searched")
            if m != 0:
                if target == nums[m-1]:
                    r = m - 1
                    m = (r + l) // 2
                else:
                    return m
            else:
                return m
        elif target < nums[m]:
            print("right discarded")
            r = m - 1
        else:
            print("left discarded")
            l = m + 1
        
    return -1

if __name__ == "__main__":
    uNums = [1,2,3,4,5,6,7,8,9,10]
    dNums = [1,2,3,3,3,4,5]
    nNums = [0,0,0,0,0]
    target = 1

    print("GO!")
    print(f"First instance of {target} in {uNums} is at index {binary_search_first(uNums, target)}")
    print(f"First instance of {target} in {dNums} is at index {binary_search_first(dNums, target)}")
    print(f"First instance of {target} in {nNums} is at index {binary_search_first(nNums, target)}")
    print("LOVE WINS!")