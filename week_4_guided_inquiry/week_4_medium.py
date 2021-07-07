# MEDIUM: Create a program that accepts a number (1-12) as input and logs to the console that number and its corresponding month. 
# For example: if the user enters the number 3, then it should return the month “March.” 
# Alert the user if they enter an invalid number (e.g. less than 1 or greater than 12).
number = input("input a number: ")

if int(number) == int(1):
    print("january")
elif int(number) == int(2):
    print("february")
elif int(number) == int(3):
    print("march")
elif int(number) == int(4):
    print("april")
elif int(number) == int(5):
    print("may")
elif int(number) == int(6):
    print("june")
elif int(number) == int(7):
    print("july")
elif int(number) == int(8):
    print("august")
elif int(number) == int(9):
    print("september")
elif int(number) == int(10):
    print("october")
elif int(number) == int(11):
    print("november")
elif int(number) == int(12):
    print("december")
elif int(number) => int(1-12):
    print("not within 1-12")

    