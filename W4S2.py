# 1. Planning Your Daily Work Schedule

print("Problem 1\n\n")  

"""
def find_task_pair(task_times, available_time):
    for o in task_times:
        diff = available_time - o
        remaining = task_times.copy().remove(o)
        if diff in remaining:
            return True
    return False

def find_task_pair(task_times, available_time):
    # do a dictionary mapping from task time to index
    times_to_indices = {task_times : range(0, len(task_times)-1)}
    # [10, 10, 20], {10: [0, 1], 20:[2]}
    # dict1 = {key: val}
    # do a loop and check if available_time - task time
    # is in the dictionary and indices arent equal
        # return true
    for e in times_to_indices:
        # Find index of match to difference, if it exists
        diff = available_time - e
        
        if (available_time - e) in times_to_indices.values() and e != 
        
    # return false
"""

def find_task_pair(task_times, available_time):
    # establish a set
    found_times = set()
    # loop through tasks in tasks times
        # check if the remainder is in the set
            # return True
    for t in task_times:
        diff = available_time - t
        if diff in found_times:
            return True
        else:
            found_times.add(t)
    return False
            
        # add current to set
    # return False
    
    
task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))

# Added test case, breaks the non-distinct assumption
# task_times_4 = [20, 20, 50, 70]
# available_time = 40
# print(find_task_pair(task_times_3, available_time))

print("\n\nProblem 2\n\n")                   
    
# 2. 
def find_smallest_gap(work_sessions):
    """
    U: input: a list of tuples that are length-2
       output: an integer representing the smallest gap between consecutive work times
    # edge case: 23 to 0
    [(1400, 1500), (2000, 2300), (0100, 2000)] 
    """
    # have a min_diff var that i keep track of 
    min_diff = float("inf")
    # I will loop through the list of work sessions
    for i in range(1, len(work_sessions)):
        # Convert first 2 and last digits to integers
        starthour = int(str(work_sessions[i][0])[:2])
        # divide last 2 by 60 to get decimal of hour
        startminutes = int(str(work_sessions[i][0])[2:]) / 60
        # add decimal to int of first 2
        starthours = starthour + startminutes
        
        endhour = int(str(work_sessions[i-1][1])[:2])
        # divide last 2 by 60 to get decimal of hour
        endminutes = int(str(work_sessions[i-1][1])[2:]) / 60
        # add decimal to int of first 2
        endhours = endhour + endminutes
        # diff = (start - end) % 24
        min_diff = min(min_diff, (starthours - endhours) % 24)

    return min_diff * 60
work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))
                   

# 3.
def calculate_expenses(expenses):
    pass

expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))


# 4.
def word_frequency_analysis(text):
    pass

text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))
