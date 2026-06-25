'''
Christian Guiang
06 11 2026
Week 2, Session 2 Practice Problems

Started: 6/11/2026
Finished: -----
Validated: -----
Last updated: 6/13/2026

Some stuff from the cheat sheet:

To make a dictionary with values from a list or other iterable:
new_dict = {key_val : value_expression for item in iterable}

    list = [1, 2, 3, 4, 5]
    squared = {num : num**2 for num in list}
    # squared --> {1:1, 2:4, 3:9, 4:16, 5:25}

    # Optional condition(s)
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_halved = {num : (num / 2) for num in list if num % 2 == 0}
    # even_halved --> {2:1, 4:2, 6:3, 8:4, 10:5}

Sets are unordered, unique collections of data. Constrast this with lists, which are ordered and can
have duplicates.

Lookup is O(1), contrasted with list lookup which is O(n).

To make a new set:
new_set = set()     # Empty set
new_set = {1, 2, 3, 4}      # Populated set (only works if you give values; turns into a dict otherwise)

Set methods:
add()       # Adds an element to the set
remove()    # Removes a given element, raises an error if not found
discard()   # ", but doesn't raise an error if not found
clear()     # Removes all elements from the set

Set operations:
a | b       # Union, or all elements in either set
a & b       # Intersection, or all common elements from both sets
a - b       # Difference, or all elements in a NOT in b
a ^ b       # Symmetric difference, or all elements in either set but NOT common from both (i.e., XOR)

    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    c = {"Alph", "Brittany", "Charlie"}

    print(f"a union b = {a|b}")
    print(f"a union b union c = {a|b|c}")
    print(f"a intersection b = {a & b}")
    print(f"a difference b = {a - b}")
    print(f"a symmetric diff b = {a ^ b}")

    # Outputs
    # a union b = {1, 2, 3, 4, 5, 6, 7, 8}
    # a union b union c = {1, 2, 3, 4, 5, 6, 7, 8, 'Alph', 'Brittany', 'Charlie'}
    # a intersection b = {4, 5}
    # a difference b = {1, 2, 3}
    # a symmetric diff b = {1, 2, 3, 6, 7, 8}
'''

# 1. Most endangered
# 
def most_endangered(species_list):
    min = float("inf")
    species = ""
    for entry in species_list:
        if entry.get("population") < min:
            min = entry.get("population")
            species = entry.get("name")
    return species

'''
2. Count endangered species(endangered_species, observe_species)

As part of conservation efforts, certain species are considered endangered and are
represented by the string "endangered_species", with each char denoting a different
endangered species. You also have a record of all observed species in the region,
represented by the string "observed_species".

Write a function "count_endangered_species()" that determines how many instances
of the observed species are also considered endangered, and returns that count.
(Keep in mind species are case-sensitive!)

Given 2 strings "endangered" and "observed", this is asking to count the # of
occurrences each char in "endangered" has in "observed".

This will involve iterating over "endangered" to scan "observed" for every
instance of the current char. If an instance is found in "observed", a count is
incremented by 1. By the end of both loops, that count is returned.

Edge cases: empty strings in either species list, no matches (return 0)

'''
def count_endangered_species(endangered_species, observed_species):
    count = 0
    
    # For every endangered species...
    for e in endangered_species:
        # Count up all of its occurrences in the observed species.
        for o in observed_species:
            if o == e:
                count += 1
    return count

'''
3. Navigating the research station
In a wildlife research station, each letter of the alphabet represents a different
observation point laid out in a single row. Given a string "station_layout" of
length 26 indicating the layout of the observation points, you start your journey
at the first observation point (index 0). Then, you move to different points
based on the points listed in string "observations".

The time taken to move from one point to the next is the absolute difference
between their indices, |i - j|.

Write a function "navigate_research_station()" that returns the total time it
takes to visit all the required observation points in the given order with one
movement.

Ex.
layout = "abcdefghijklmnopqrstuvwxyz"
observations = "cba"

navigate_research_station(layout, observations) --> 4
# a --> c = 2, c --> b = 1, b --> a = 1; 2 + 1 + 1 = 4.

This is asking to find the sum of the distances between characters in a string
"observations", depending on their positions in another string "station_layout".
Consequently, it's asking to have some way to keep track of two adjacent chars
in a string, then doing an operation using their values mapped to them in a
dictionary, here given as their index in a string.

Given that, it would be helpful to map each letter in the layout to its index
value using a dictionary; that way, we could more easily access and do
calculations with their corresponding values. The "enumerate()" function
could be useful for this, since it adds a counter to every element passed to it
via list. From there, we could turn it into a dictionary, with the bonus of
being able to swap the index and value (ex. a:0 instead of 0:a).

After that's done, starting with a count "dist" at 0 and a previous char tracker
"prevPoint" at 0, we can iterate through all the points in "observations",
adding the absolute difference between prevPoint and the current point.

Edge cases: Empty strings for observations
'''

def navigate_research_station(station_layout, observations):
    dist = 0
    prevPoint = 0
    index_map = {char : station_layout.index(char) for char in station_layout}
    for o in range(len(observations)):
        # Ignore that comment on the next line, it's just so Pylance doesn't 
        dist += abs(index_map.get(observations[o]) - index_map.get(station_layout[prevPoint])) #type: ignore
        # Set the previous point to the spot in the layout where the current char is found.
        prevPoint = station_layout.index(observations[o])
    return dist

'''
4. Prioritizing Endangered Species Observations
In your work with a wildlife conservation database, you have two lists:
"observed_species" and "priority_species". The elements of "priority_species"
are distinct, and all elements in it are also in "observed_species".

Write a function "prioritize_observations()" that sorts the elements of
"observed_species" such that the relative ordering of items in it matches
that of "priority_species". Any species not in "priority_species" should
be placed at the end of "observed_species" in ascending order.

Contrary to what I first thought, this problem is asking to return a LIST of
elements, not a set. Namely, it asks for a list made of two parts:

1. All occurrences of species matching those in "priority_species", from
    "observed_species", sorted by relative order in "priority_species".
2. The remaining elements of "observed_species", sorted in ascending order.

So, let's do this:

Make two lists, one for each group listed above using a loop over all elements
in "observed_species" and a conditional with "in priority_species". Call these
"left" and "right". Use "sorted()" on "left" with a key of the indices in 
"prioritized_species". Then, use "sorted()" on "right" as is to get it in
ascending order. Finally, return "left.extend(right)" to return
the lists stitched together.

Note that "filter()" can be used to get the outliers instead of using sets.
However, I'm choosing not to use "filter()" so I have a chance to use sets.

Edge cases: empty lists for either
'''
def prioritize_observations(observed_species, prioritized_species):
    # Can't use "non-priority" or "not-priority" since they have keywords...
    left = []
    right = []
    # Make the groups
    for species in observed_species:
        if species in prioritized_species:
            left.append(species)
        else:
            right.append(species)
    # Note that "sorted()" returns a sorted iterable, while "extend()" returns None.
    left = sorted(left, key = lambda o : prioritized_species.index(o))
    right = (sorted(right))
    left.extend(right)
    return left


'''
5. Calculating Conservation Statistics
You are given a 0-indexed integer array "species_populations" of even length, where
each element represents the population of a particular species in a wildlife reserve.

As long as "species_populations" is not empty, you must:

1. Find and remove the species with the minimum population.
2. Find and remove the species with the maximum population.
3. Calculate the average population between the two.
(In the case of ties, remove any species that's tied.)

Write a function "distinct_averages()" that returns all the distinct average values
derived from this process.

The problem is straightforward in asking to iterate through an array removing the min
and max elements where population is concerned, then asking to return the number of
distinct averages derived from those two elements.

Since the iteration must go until the array is empty, it's best to use a while loop
with "species_populations != None" or an equivalent expression as a condition. Then,
each iteration of the loop, the min and max can be removed with "pop()", continuing
until the array is empty. Holding the averages is done using a var "aves", and new
averages can be added only if they're not in "aves" already.

Edge cases: Empty list "species_populations", but this just returns 0.
'''
def distinct_averages(species_populations):
    aves = []
    while len(species_populations) != 0:
        # Long!
        newAve = (species_populations.pop(species_populations.index(max(species_populations))) +
                  species_populations.pop(species_populations.index(min(species_populations)))) / 2
        if newAve not in aves:
            aves.append(newAve)
    print(aves)
    return len(aves)

# Test here

if __name__ == "__main__":
    species_populations1 = [4,1,4,0,3,5]
    species_populations2 = [1,100]

    print(distinct_averages(species_populations1))
    print(distinct_averages(species_populations2)) 

