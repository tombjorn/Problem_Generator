import random
import string

chars = string.ascii_letters

ProbType = {
    1 : "Reverse array of given type",
    2 : "Sort array of given type in ascending order",
    3 : "Sort array of given type in descending order",
    4 : "Check for duplicates in an array of strings",
    5 : "Check for Palindromes in an array of strings",
    6 : "Check if given string is pallindrome"
    # 6 : "Recursive function that counts up from 0 to n",
    # 7 : "Recursive function that counts down from n to 0",
}

animArr = ['dog', 'cat', 'elephant', 'mouse', 
'bird', 'moose', 'rabbit', 'whale',
'rat', 'shark', 'lizard', 'snake']

palinArr = ['yellow', 'racecar', 'palindrome', 
'ooooo', 'kayak', 'deified', 'rotator', 'peep', 
'red', 'tube', 'setting', 'waiting', 'hello']

# generate random array INTS for array questions
def intsArr(n):
    arr = []
    r = range(n)
    for i in r:
        arr.append(random.randint(0, 100))
    return arr

# generate random array CHAR for array questions
def charsArr(n):
    arr = []
    r = range(n)
    for i in r:
        arr.insert(i, random.choice(chars))
    return arr

# generate array of random animals from animalArr
def animalsArray(n):
    arr = []
    r = range(n)
    for i in r:
        arr.insert(i, random.choice(animArr))
    return arr

# generate array of random palindromes from palinArr
def palindromeArray(n):
    arr = []
    r = range(n)
    for i in r:
        arr.insert(i, random.choice(palinArr))
    return arr

# pick a random string from palinArr
def palindromePicker():
    str = random.choice(palinArr)
    return str

# call function corresponding to dictionary key
def fileWriter(r):
    if r == 1 or r == 2 or r == 3:
        x = random.randint(0, 1)
        if x == 0:
            arr = intsArr(10)
            return 'arr = {} \n'.format(arr)
        else:
            arr = intsArr(10)
            return 'arr = {} \n'.format(arr)
    elif r == 4:
        arr = animalsArray(6)
        return 'arr = {} \n'.format(arr)

    elif r == 5:
        arr = palindromeArray(6)
        return 'arr = {} \n'.format(arr)

    elif r == 6:
        str = palindromePicker()
        return 'str = {} \n'.format(str)
    
