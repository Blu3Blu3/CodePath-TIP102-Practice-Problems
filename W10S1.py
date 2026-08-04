# Week 10, Session 1

# 1. Graphing Flights

'''
The following graph represents the different flights offered by CodePath Airlines. 
Each node or vertex represents an airport (JFK - New York City, LAX - Los Angeles, DFW - Dallas Fort Worth, and ATL - Atlanta), and 
an edge between two vertices indicates that CodePath airlines offers flights between those two airports.

Create a variable flights that represents the undirected graph below as an adjacency dictionary, where each node's value is 
represented by a string with the airport's name (ex. "JFK").

JFK ----- LAX
|
|
DFW ----- ATL
'''

flights = {
    'JFK' : ['DFW', 'LAX'],
    'LAX' : ['JFK'],
    'DFW' : ['ATL', 'JFK'],
    'ATL' : ['DFW']
}

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])
# Example Output:

# ['JFK', 'LAX', 'DFW', 'ATL']
# [['LAX', 'DFW'], ['JFK'], ['ATL', 'JFK'], ['DFW']]
# ['LAX', 'DFW']

#2. 
'''
As a flight coordinator for CodePath airlines, you have a 0-indexed adjacency list flights with n nodes where each node represents the ID of a 
different destination and flights[i] is an integer array indicating that there is a flight from destination i to each destination in flights[i]. 
Write a function bidirectional_flights() that returns True if for every flight from a destination i to a destination j 
there also exists a flight from destination j to destination i. Return False otherwise.
'''
def bidirectional_flights(flights):
    '''
    (U)
    Given a graph "flights" where each element "flights[i]" is an int array indicating that there is a connection from i to another node, return True if every connection in flights is bidirectional.

    Input:
        - flights ([[int]])
    Output:
        - True if all edges in flights are bidirectional, False otherwise
    Edge cases:
        - flights is an empty list, return False
        - flights[0] = [0, 1, 2] or index list has its own index; probably not going to happen.

    (P)
    for ind in range(len(flights)):
        for connection in range(len(flights[ind]))
            if ind not in flights[connection]
                return false
    return true 
    '''
    for index in range(len(flights)):
        for connection in flights[index]:
            if index not in flights[connection]:
                #print(f"index = {index}, connection = {connection}")
                return False
    return True


# Example Usage:
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))
# Example Output:

# True
# False

# 3. Finding Direct Flights
'''
Given an adjacency matrix flights of size n x n where each of the n nodes in the graph represent a distinct destination and n[i][j] = 1 indicates 
that there exists a flight from destination i to destination j and n[i][j] = 0 indicates that no such flight exists. 

Given flights and an integer source representing the destination a customer is flying out of, 
return a list of all destinations the customer can reach from source on a direct flight. 
You may return the destinations in any order.

A customer can reach a destination on a direct flight if that destination is a neighbor of source.
(U) 
    n[i][j] = 1 indicates that a flight exists 
    n[i][j] = 0 indicates that a flight doesn't exist 
    Input: Source - Integer
    Output: List of the distinations that can be reached from source
    Edge Cases:
        - Flights is Empty, return empty list
        - Values aren't 0 or 1, return empty list
        - Source isn't greated than or equal len(flifhts) 
(P) 
    - Create a new list that ho;ds the destinations that can be reached from source
    - For loop and If statement that checks if flight[i][j] == 1 or 0,
    - If flight[i][j] equals 1, then we append the index of # i*j? 

'''
def get_direct_flights(flights, source):
    distinations = []
    for index in range(len(flights[source])):
        if flights[source][index] == 1:
            distinations.append(index)
    return distinations 

flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],# index 1, can go 0 123
            [1, 1, 0, 1],
            [0, 0, 0, 0]]

# print(get_direct_flights(flights, 2))
# print(get_direct_flights(flights, 3))
# Example Output:

# [0, 1, 3]
# []

# Problem 4: Converting Flight Representations
'''
Given a list of edges flights where flights[i] = [a, b] denotes that there exists a bidirectional flight (incoming and outgoing flight) from city a to city b, 
return an adjacency dictionary adj_dict representing the same flights graph where adj_dict[a] is an array denoting there is a flight from city a to each city in adj_dict[a].

U:
    input: 
        list of edges "flights"
    output: 
        dictionary showing bidirectional flight

    edge case: 
        empty list = empty dictionary 
P
    create empty dictionary 
    loop over "flights", if city a exist in city b - vice versa, add to dictionary 
'''
def get_adj_dict(flights):
    adj_dict = {}

    for index in range(len(flights)):
        for bidirectional_flight in flights[index]:
            



flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))
# Example Output:

# {
#     'Cape Town': ['Addis Ababa', 'Cairo'],
#     'Addis Ababa': ['Cape Town', 'Lagos'],
#     'Lagos': ['Cairo', 'Addis Ababa'],
#     'Cairo': ['Lagos', 'Nairobi', 'Cape Town'],
#     'Nairobi': ['Cairo']
# }