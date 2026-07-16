"""
Christian Guiang
Week 7, Session 2
July 16, 2026
"""

def canConstruct(ransomNote: str, magazine: str):
    """
    Given two strings ransomNote and magazine, return true if ransomNote
    can be constructed by using the letters from magazine and false
    otherwise.
    
    (U)
    Given two strings ransomNote and magazine, return true if the whole
    string ransomNote can be made from the letters in magazine.
    
    Input:
    -   ransomNote (str), the string to recreate
    -   magazine (str), the string holding all available characters to
            recreate from
    Output:
    -   True or False
    
    Edge cases:
    -   ransomNote is longer than magazine; skip checks and return False
    -   ransomNote is empty; return True?
    
    (M)
    To organize the available characters in magazine, we can use buckets
    in the form of dictionary entries mapped to each character. For
    every instance of a character in magazine, we can store it as 1 added
    to that character's corresponding entry (starting at 0).
    
    (P)
    First, create an empty dictionary "buckets" to hold the frequencies of
    each character in magazine. Then, iterating through magazine letter by
    letter, add 1 to a character's entry in buckets each time it's come
    across.
    
    By the end, each character's frequency will be mapped, and a second
    loop to iterate through ransomNote can be used to check if there are
    enough instances of each character needed held in buckets. This check
    can be done by subtracting 1 from the entry's value each time a given
    character is found in ransomNote.
    
    Return False if a character is needed that isn't found in buckets or
    doesn't have enough instances (pulled while 0). Return True otherwise.
    """
    # I love lambdas!
    buckets = {c : magazine.count(c) for c in magazine}
    for c in ransomNote:
        if c not in buckets or buckets.get(c) <= 0:
            return False
        else:
            buckets[c] -= 1
    return True
    
ran = "aaa"
magazine = "1234567890 abcdefghijklmnopqrstuvwxyz"
print(f"Does \"{magazine}\" contain the letters used to make \"{ran}\"?", canConstruct(ran, magazine))
    
    
    
    
    