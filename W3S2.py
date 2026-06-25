'''
Christian Guiang
06 18 2026
Week 2, Session 2 Practice Problems

Started: 6/18/2026
Finished: -----
Validated: -----
Last updated: 6/18/2026

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
'''

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

