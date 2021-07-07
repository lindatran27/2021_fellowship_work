# VERY EASY: Write a function named min that takes two arguments and returns their minimum.

def min(a, b):
    if a <= b:
        return a
    else:
        return b

a = 12
b = 25

print(min(a, b))