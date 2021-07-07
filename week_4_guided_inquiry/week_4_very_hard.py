# VERY HARD: Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. 
# If found in the array return its index, otherwise return “The input is not on this list”

# You may assume no duplicate exists in the array.

# Hint:  Use a function. Use the built in method .index( ) and/or for loops. 
# Review your lesson on Arrays to aid in working through this problem. 
anArray = [0, 1, 2, 4, 5, 6, 7]

targetValue = input("what is your target value?")

if int(targetValue) in anArray:
    print(targetValue," is in the list")
else: 
    print(targetValue," is not in the list") 