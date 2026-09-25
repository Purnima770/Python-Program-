# program to accept a number from keyboard and test whether it is even or odd

x = int(input("Enter a number: "))
if x % 2 == 0:
    print(x, " is an even number")
else:
    print(x, " is an odd number")