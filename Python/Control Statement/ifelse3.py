# program to test whether a given number is in between 1 and 10

x = int(input("Enter a number: "))
if x > 1 and x < 10:
    print("You typed", x, "The number is in between 1 and 10")
else:
    print("You typed", x, "The number is not in between 1 and 10")