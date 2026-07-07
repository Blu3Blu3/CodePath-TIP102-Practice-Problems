"""
Christian Guiang
"Do you ever feel, like a plastic bag?"
Started: 7/4/2026
Finished: -----
Validated: -----
Last updated: 7/4/2026

* Remember to turn on word wrap in VSCode!

This week introduced Object Oriented Programming, which in short is the concept of using classes to create objects that can hold states and behaviors, and do more than plain data types. The objects are based on real-world objects or data types, so you could have things like a Person, a Car, or a BankAccount.

In general, you want to create objects when:
-   You need to group related data and methods together in one place.
-   You need to keep track of states across individual instances.

To make an object, you need to first make a class using the "class" keyword as you would "def" for a function. Inside the resulting code block, you need a constructor, named "__init__", to initialize new objects of the class you create. In there, you can set all the member variables you want by using "self.var = value", where "self" is a parameter referring to the object calling the function. It's like the "this" keyword in other languages. After, you can add any functions that would grant the class more functionality by using "def" as usual.

Ex.
# Let's make a class for a cat, and call it "Cat". Class names are usually capitalized.
class Cat:
    # This is called when a new Cat object is created, to set the member values right away.
    # You can't overload functions in Python, at least using the same names and # of parameters.
    # Instead, it's helpful to use default values, especially here in constructors.
    def __init__(self, name = "Steppy", age = 1, breed = "Bombay"):
        self.name = name
        self.age = age
        self.breed = breed

    # Let's also make a function for Cat objects to introduce themselves.
    def introduce(self):
        return f"Hello! My name is {self.name}, and I'm a {self.breed} who's {self.age}. Mew!"

This week also introduced Linked Lists, a data collection type that's comprised of Nodes instead of indices. These Nodes are objects of the Node class, and typically only have two member variables: a value that the Node holds, and a pointer to the next Node in the list, usually called "next" or "tail".

Linked Lists are accessed from the head, or the first Node in the list. To traverse through one, you need to follow the head's "next" pointer to the next Node, and so on until the end, where "next" would be set to nothing (None). These Linked Lists are "singly linked", only being able to point to the next Node. Some are instead "doubly linked", where each Node also has a pointer to the Node before it, often called "head" or "prev".

Given the way Linked Lists work, you must traverse through them fully to find the length, unlike arrays where you can just call "len()". This turns out to be O(n) (which is the same as finding the length of an array normally, but still). Same goes for adding, removing, or updating an element in a Linked List, since the traversal to get to a target element is unavoidable.

Ex.
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

head = Node("A")
mid1 = Node("B")
mid2 = Node("C")
end = Node("D")

head.next = mid1
mid1.next = mid2
mid2.next = end

# While loops are most helpful when traversing Linked Lists since they're not dependent on range functions to know when to stop, and with Linked Lists, you most likely don't know the length, so you can't use "range(len())" or such.
currentNode = head
while currentNode.next != None:
    print(currentNode.value)
    # Make sure you have this to prevent the loop from iterating infinitely on the head.
    currentNode = currentNode.next

Problems with Linked Lists may require you to keep track of previous nodes for the sake of "healing" parts where nodes were removed or so. In these cases, you may greatly benefit from keeping temporary nodes that hold the values of nodes you want to track. Otherwise, you'd likely have to deal with a lot of edge cases.

Also, in any type of Linked List, you may come across cycles caused by nodes pointing to each other in a loop.

Ex.
head = Node("Flower Fields")
mid1 = Node("Ghoulish Grove")
mid2 = Node("Glimmer Glaciers")
mid3 = Node("Gusty Gulch")
end = Node("Silver Summit")

head.next = mid1
mid1.next = mid2
mid2.next = mid3
mid3.next = mid1
# Nothing points to end, and mid3 creates cycle from mid1 --> mid2 --> mid3 --> mid1.

Some problems may ask you to find cycles like these, and for that, you can employ slow-fast pointers. These are two pointers moving at different speeds through the Linked List that, when they point to the same node, show that a cycle is present. You'll often have the slow pointer moving 1 node at a time, while the fast pointer moves 2 nodes at a time.

Ex.
In head --> mid1 --> mid2 --> mid3 --> mid1 --> ...:
    1. Start slow and fast at head.
    2. slow = mid1, fast = mid2, no match
    3. slow = mid2, fast = mid1, no match
    4. slow = mid1, fast = mid3, match. Cycle found.
"""

### SET 1 ###

# 1. New Horizons
# Given class code
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

# Instantiate your villager here
"""
Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named "apollo".

The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".

(U)
This is asking to create a new Villager object "apollo" using the values given.
    Input: None, this isn't a function
    Output: None, this isn't a function

(P)
Since the constructor is already made in the Villager class, we can just call that as the value to initialize a var "apollo" with. We just need to use the given parameter values.
"""
apollo = Villager("Apollo", "Eagle", "pah")

# Test 1
print(f"Hey, nice to meet you! I'm {apollo.name}! Looks like I'm the first {apollo.species} to land here, {apollo.catchphrase}.")

# 2. Greet Player
"""
Using the Villager class from Problem 1, add the following greet_player() method to your existing code:

def greet_player(self, player_name):
    return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

Create a second instance of Villager in a variable named bones.
The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".

Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.

(U)
This is asking to add a new method "greet_player(player_name)" to the Villager class that prints a greeting statement using a given name and the Villager object's member values.
    Input: player_name (string)
    Output: A greeting (string)

(P)
This can be done by adding a function as normal, just inside the Villager class. It'll just return a formatted string like above using "self.name" and "self.catchphrase" where the name and catchphrase go.

As for the new Villager, they can be constructed as in Problem 1, using the constructor with custom parameters.

...The code is already written in the directions, too, so there's not much to be done, really...
"""

bones = Villager("Bones", "Dog", "yip yip")
print(bones.greet_player("Isabelle"))

# 3. Update Catchphrase
"""
In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.

Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".

(U)
This is asking to change the catchphrase attribute in "bones" from "yip yip" to "ruff it up".

(P)
Since the catchphrase attribute for Villager objects is public, we can just set bones.catchphrase to "ruff it up" as we would any other variable.
"""
bones.catchphrase = "ruff it up"
print(bones.greet_player("Isabelle"))

# 4: Set character
"""
In the previous exercise, we accessed and modified a player's catchphrase attribute directly. Instead of allowing users to update their player directly, it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.

    If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase and print "Catchphrase updated".
    Otherwise, it should print out "Invalid catchphrase".

Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.

(U)
This is 
"""
