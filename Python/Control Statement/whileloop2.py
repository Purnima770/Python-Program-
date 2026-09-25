# program to display even numbers betweem 100 and 200

# x=100
# while x>=100 and x<=200:
#     print(x)
#     x+=2



# program to display even number between m and n

m, n = [int(i) for i in input("Enter minimum and maximum range: ").split(',')]
x=m
if x%2!=0:
    x=x+1

    while x>=m and x<=n:
        print(x)
        x+=2