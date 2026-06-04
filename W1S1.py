'''
Christian Guiang
Week 1, Session 1
Started: 6/4/2026
Finished: -----
Validated: -----
Last updated: 6/4/2026

Hi! These problems are going to be paraphrased from the course and answered in both the comments and code.
Once all the problems are solved, code to test it will be added at the bottom of this file; from there,
feel free to run this and validate that everything works.

By the way, the comments will describe my thought process following the "Understand, Plan, Implement"
framework "UPI", as practice for doing the same in a live interview.
'''

'''
1. Hundred Acre Wood
Write a function "welcome()" that prints the string "Welcome to the Hundred Acre Wood!"

This is simply using "print()" inside a function. 
'''
def welcome():
  print("Welcome to the Hundred Acre Wood!")

'''
2. Greeting
Write a function "greeting()" that accepts a single parameter, a string "name", and prints:
"Welcome to the Hundred Acre Wood <name>! My name is Christopher Robin."

This is asking for a string to be added in the middle of another to create a greeting.
To do this, either a formatted string "f-string" or concatenating pieces "Welcome..." + name + "! My name..."will work.
'''
def greeting(name):
  print(f"Welcome to the Hundred Acre Wood {name}! My name is Christopher Robin.")

'''
3. Catchphrase
Write a function "print_catchphrase()" that accepts a string "character" as a parameter and prints their
catchphrase as outlined here:
"Pooh" -> "Oh bother!"
"Tigger" -> "TTFN: Ta-ta for now!"
"Eeyore" -> "Thanks for noticing me."
"Christopher Robin" -> "Silly old bear."
Anything else -> "Sorry! I don't know <character>'s catchphrase!"

This is asking for specific strings to be printed based on what "character" is.
Since there are specific cases to check "character" for, this requires either a switch statement or a series
of conditional checks. I'll use a switch statement for better clarity.
'''
def print_catchphrase(character):
  match character:
    case "Pooh":
      print("Oh bother!")
    case "Tigger":
      print("TTFN: Ta-ta for now!")
    case "Eeyore":
      print("Thanks for noticing me.")
    case "Christopher Robin":
      print("Silly old bear.")
    case _:
      print(f"Sorry! I don't know {character}'s catchphrase!")

'''
4. Return Item
Implement a function "get_item()" that accepts a 0-indexed list items and a non-negative integer x, and
returns the element at index x in items. If x is an invalid index, return None.

This is simply asking to return items[x], or None if x is out of bounds.
Python doesn't have a method that automatically returns None if a target index is OOB, so I'm adding a
condition to check for that.
'''
def get_item(items, x):
  if(x < len(items) and x >= 0):
    return items[x]
  else:
    return None

'''
5. Total Honey
Write a function "sum_honey()" that accepts a list of integers "hunny_jars" and returns the sum of all
elements in the list. Do not use "sum()".

Since "sum()" isn't allowed, this is asking us to iterate through the list "hunny_jars" and add up all the
values with some catch variable. A for loop would be easiest to implement this in.
'''
def sum_honey(hunny_jars):
  sum = 0
  for h in hunny_jars:
    sum += h
  return sum

'''
6. Double Trouble
Write a function "doubled()" that accepts a list of integers "hunny_jars" and multiplies each element in
the list by two. Return the doubled list.

This follows the same implementation as problem 5, only multiplying each element iterated over instead of
adding it to a sum variable. However, multiplying the elements in the list given will carry over into the
rest of the code unless a copy of the list is used instead. So, instead of multiplying the elements in
"hunny_jars" directly, I'll copy it into another variable and multiply over that.
'''
def doubled(hunny_jars):
  ret = hunny_jars.copy()
  for h in range(len(ret)):
    ret[h] *= 2
  return ret







