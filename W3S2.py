"""
Christian Guiang
Week 3, Session 2 Practice Problems
Started: 6/19/2026
Finished: -----
Validated: -----
Last updated: 6/20/2026

TODO: Change all camelCaseVariable names to underscore_variable names.

Some stuff from the cheat sheet:

Stacks are data collections that follow a "last in, first out" policy. Only the top/first element can be interacted with by adding
a new element or removing/"popping" it.

Python doesn't have a dedicated object for stacks, but lists fill the role well enough with the methods "append()" and "pop". They're
also both O(1), so access and updates are very fast!

Try using stacks with problems where reversing order or backtracking are involved.

Some methods with stacks:
    - stack.append(e) = Appends an element "e" to the end.
    - stack.pop() = Removes and returns the last added element.

Queues are data collections that follow a "first in, first out" policy. You can append new elements at any time, but the first element
appended will still be the first to be removed when you call for a removal.

Python uses "deque", or "double-ended queue", objects for this. The "double-ended" part refers to the ability to append and pop from
the left and right ends of the queue. Realistically, you're only going to pick one side and work with that, but it's still nice to
have the option.

You must import "deque" from "collections" using "from collections import deque".

Some methods with deque:
    - queue = deque(): Makes a new queue.
    - queue.append(e): Appends an element to the right.
    - queue.popleft(): Pops the leftmost element. Use this with append() in queues moving left.
    - queue.appendleft(e): Appends an element to the left.
    - queue.pop(): Pops the right most element. Use this with appendleft() in queues moving right.
    - queue.extend([a, b, c, ...]): Appends elements to the right in the order given.
    - queue.extendleft([a, b, c, ...]): Appends elements to the left in the order given.

    - queue.rotate(n): Rotates the queue "n" spaces clockwise (ex. [1, 2, 3, 4] )
    - queue.reverse(): Reverses the order of the queue.
    - queue.count(e): Returns the # of times element "e" appears in the queue.
"""

# 1. Manage Performance Stage Changes
# NOTE: This actually fails in Python versions below 3.10, because "match" is a recent addition.
def manage_stage_changes(changes):
    scheduled = []
    canceled = []
    for c in changes:
        cSplit = c.split()
        match cSplit[0]:
            case "Schedule":
                scheduled.append(cSplit[1])
            case "Cancel":
                canceled.append(scheduled.pop())
            case "Reschedule":
                scheduled.append(canceled.pop())
            case _:
                continue
    return scheduled

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

# Source - https://stackoverflow.com/a/44852626
# Posted by Shivank Tibrewal
# Retrieved 2026-06-18, License - CC BY-SA 3.0

#foo = [(list of tuples)]
#foo.sort(key=lambda x:x[0]) #To sort by first element of the tuple


from collections import deque

def process_performance_requests(requests):
    queue = []
    requests.sort(key = lambda x : x[0], reverse=True)
    
    for i in requests:
        queue.append(i[1])
    
    return queue

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

def collect_festival_points(points):
    
    total = 0
    while points:
        total += points.pop()
        
    return total
        
    
print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 

def booth_navigation(clues):
    journey = []
    for clue in clues:
        if clue == "back" and len(journey) > 0:
            journey.pop()
        elif clue != "back":
            journey.append(clue)
        else:
            continue
    return journey

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 

def merge_schedules(schedule1, schedule2):
    pointer1 = 0
    pointer2 = 0
    final = ""
    
    while pointer1 < len(schedule1) and pointer2 < len(schedule2):
        final += schedule1[pointer1]
        final += schedule2[pointer2]
        pointer1 += 1
        pointer2 += 1
    
    if len(schedule1) > pointer1:
        final += schedule1[pointer1:]
    if len(schedule2) > pointer2: 
        final += schedule2[pointer2:]
        
    return final

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 

### SET 2 ###

"""
1. Final Costs After a Supply Discount
You are managing the budget for a global expedition, where the cost of supplies is represented by an integer array
"costs", where costs[i] is the i-th supply item's cost.

There is a special discount available during the expedition, where purchasing the i-th item gives a discount
equivalent to costs[j], where j is the minimum index such that j > i and costs[j] <= costs[i]. If no such j exists,
no discount is given.

Return an int array "final_costs" where final_costs[i] is the final cost you will pay for the i-th supply item,
considering the special discount.
---
This problem is asking to iterate through a list of costs, scanning through the costs after the currently checked one
for the opportunity to apply a discount.

In other words, for every element i, append either i or (i-j), where j is some element after i where j <= i,
depending on such an element exists.

To solve this, it was suggested to use a stack, but there doesn't really seem to be a good use for one outside of having
a stack hold the values to return. The "append()" method is really handy, after all.

Instead, let's either make a copy of the array "costs" or make a new list. Then, do the following:

1. Iterate through "costs" or its copy depending on your choice, preferably using a for loop.
2. For each element i, have a second for loop running from the next element to the end check for an element j
    where j <= i.
    - If j exists, either add (i-j) to your return list, or subtract j from element i. Then, break the second loop.
    - Otherwise, add i to your return list, or do nothing.
3. Once the outer loop finishes and "costs" has been iterated through, return either your return list or the copy of
    "costs" that was updated in the outer loop.
    - Note that either method should have the same space requirement.
    
Edge cases: "costs" is length 1 or less, return "costs"
"""
# Validated 6/20/2026
# print(final_supply_costs([8, 4, 6, 2, 3]))
# print(final_supply_costs([1, 2, 3, 4, 5]))
# print(final_supply_costs([10, 1, 1, 6]))
def final_supply_costs(costs):
    discounted = costs.copy()
    for c in range(len(discounted)):
        for d in discounted[c+1:]:
            if d <= discounted[c]:
                discounted[c] -= d
                break
    return discounted

'''
2. Find First Symmetrical Landmark Name
During your global expedition, you encounter a series of landmarks, each represented by a string in the array
"landmarks". Find an return the first symmetrical landmark name, or "" if no such name exists.

This is asking to find the first palindrome in a list of strings, or the empty string "" if none exist.

The Two Pointer Technique is suggested here, and I wholeheartedly agree with using it. It'd be easiest to find
palindromes by having two pointers starting at either end of a given string and working their way towards the middle.
Let's call these "f" and "l". Then:

1. Iterate through "landmarks", setting "f" to 0 and "l" to the length of the current string "str" - 1.
2. Set a flag "isPalindrome" or so to True.
3. Use a while loop with condition (f < l) to check if str[f] == str[l].
    - If so, increment f by 1 and decrement l by 1.
    - If not, set the flag to False and break the loop.
4. Once the while loop is over, if the flag is still True, return the current string "str".
5. If no palindromes were found in "landmarks" (i.e.,  the outer loop ended), return "".

Edge cases: Empty list "landmarks", return ""; list with multiple palindromes, return the first.
'''
# Validated 6/20/2026
# print(first_symmetrical_landmark(["dunsparce", "clefable", "girafarig", "slowpoke", "farigiraf"]))
# print(first_symmetrical_landmark(["goop", "gup", "geep"]))
# print(first_symmetrical_landmark([]))
def first_symmetrical_landmark(landmarks):
    for mark in landmarks:
        f = 0
        l = len(mark) - 1
        is_palindrome = True
        while f < l:
            if mark[f] != mark[l]:
                is_palindrome = False
                break
            else:
                f += 1
                l -= 1
        if is_palindrome:
            return mark
    # If no palindromes found, return ""
    return ""

"""
3. Terrain Elevation Match
During your global expedition, you are mapping out the terrain elevations, where the elevation of each point is
represented by an integer. You're given a string "terrain" of length n, where:

    - terrain[i] == 'I' indicates the elevation of the i-th point is lower than that of the (i+1)-th point.
    - terrain[i] == 'D' indicates the elevation of the i-th point is higher than that of the (i+1)-th point.
    
In other words, if it's 'I', the elevation of the next point is an increase. If it's 'D', the elevation of the next
point is a decrease.

Your task is to reconstruct the elevation sequence and return it as a list of integers. If there are multiple valid
sequences, return any of them.

* Note that all the example outputs have unique elements, so try not to repeat values. *

This is asking to create a sequence of n+1 integers such that for any index "i" in the given string "terrain",
sequence[i] < sequence[i+1] if terrain[i] = 'I', and sequence[i] > sequence[i+1] if terrain[i] = 'D'. Also, all
elements in the sequence should be unique.

It's suggested to use two variables, one to track the smallest available number and one for the largest. When
the elevation increases, you can assign the smallest number, and when the elevation decreases, you can assign the
largest number. That way, you don't have to go back and adjust previous elements while keeping uniqueness.

Given that hint, it seems that this can be done by establishing a range of possible numbers 0-n, where n is the length
of "terrain", then filling an array "sequence" with numbers from that range. Namely, they'll be added as follows:

1. Establish a range using minimum available value "min" = 0, and maximum available value "max" = len(terrain) + 1.
2. Iterate through "terrain" using a loop, say "for i in range(len(terrain))" since we're working with indices.
    - If terrain[i] == 'I', append min to the sequence, then increment min by 1.
    - If terrain[i] == 'D', append max to the sequence, then decrement max by 1.
3. Once the loop is over, append either min or max to the end, since they'll end up being the same number.
4. Return the sequence.

The idea here is to start with the extreme values to prevent the need to retroactively adjust elements in the sequence.
In this sense, the reverse could work too, where you start from a middle valued work your way backwards through
"terrain", but only if you're feeling silly I guess.
"""
# Validated 6/20/2026
# print(terrain_elevation_match("IDID"))
# print(terrain_elevation_match("III"))
# print(terrain_elevation_match("DDI")) 
def terrain_elevation_match(terrain):
    min = 0
    max = len(terrain)
    seq = []
    for t in terrain:
        match t:
            case 'I':
                seq.append(min)
                min += 1
            case 'D':
                seq.append(max)
                max -=1
            case _:
                print(f"Invalid character \'{t}\'.")
    seq.append(max)
    return seq






