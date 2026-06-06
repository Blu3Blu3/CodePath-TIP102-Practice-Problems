'''
Christian Guiang
Week 1, Session 2
understand match plan implement review evaluate
Started: 6/4/2026
Finished: -----
Validated: -----
Last updated: 6/6/2026

Hello! This is the part where I write notes!

Understand
    - Ask clarifying questions to better understand what the interviewer is asking
    - Generate some sample input/output
    - Identify edge cases
    - Explore tradeoffs in memory, space, etc.
Plan
    - Describe your overall approach in 1-2 sentences
    - Write them down in plain English
    - Each step should be simple and clear
Implement
    - Translate your plan into code (this should be easy if it's a good plan)
    - Look up any basic Python you may need
'''

# Set Version 1

'''
1. Reverse Sentence
Write a function "reverse_sentence()" that takes in a string "sentence" and returns
the sentence with the order of the words reversed, like so:

"tubby little cubby all stuffed with fluff" --> "fluff with stuffed all cubby little tubby"
"Pooh" --> "Pooh"
'''
def reverse_sentence(sentence):
    # 
    words = sentence.split(' ')
    ret = ""

    for w in range(len(words) - 1, 1, -1):
        print(f"Joining \'{words[w]}\'...")
        ret += words[w]
        ret += ' '

    ret += (words[0])

    return ret
        

'''
2. Goldilocks Number


'''

'''
3. 
'''

'''
4. Sum of Digits

Edge cases: empty, non-ints
'''
def sum_of_digits(num):
    sum = 0

    while num > 0:
        sum += num % 10
        num = num // 10

    return sum

'''
5. 

Edge cases: empty, non-operations
'''
def final_value_after_operations(operations):
    tigger = 1
    for o in operations:
        match o:
            case "bouncy" | "flouncy":
                tigger += 1
            case "trouncy" | "pouncy":
                tigger -= 1

    return tigger

'''
6. Acronym

Edge cases: len(s) != len(words)
'''
def is_acronym(words, s):
    for i in range(len(s)):
        if s[i] != words[i][0]:
            return False
    return True

# 

# Test here
if __name__ == "__main__":
    words = ["christopher", "robin", "milne"]
    s = "crm"
    print(is_acronym(words, s))

    words = ["christopher", "robin", "milne"]
    s = "cr"
    print(is_acronym(words, s))




