print("GHOST GAME!")
print("Three doors ahead of you, and a ghost behind one of them")
print("Which door do you want to open?")
door = input("1, 2, or 3? : ")
score = 0

from ast import If
from fileinput import close
import random
from time import time
from tracemalloc import stop
value = random.randint(1, 3)
print(value)
if door == "1":
    print("did you make it?")
    score += 10

elif door == "2":
    print("did you make it?")
    score = 0

elif door == "3":
    print("did you make it?")
    score += 10

print("your score is 10 would you like to try again?")
door = input("yes, no : ")
if door == "no":
    quit()

if door == "yes":
 print("ok")
print("GHOST GAME!")
print("Three doors ahead of you, and a ghost behind one of them")
print("Which door do you want to open?")
door = input("1, 2, or 3? : ")
score = 0 
import random
value = random.randint(1, 3)
print(value)
if door == "1":
    print("did you make it?")
    score += 10

elif door == "2":
    print("did you make it?")
    score = 0

elif door == "3":
    print("did you make it?")
    score += 10
    print("if you did make it your score is now  20")
   