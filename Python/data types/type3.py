# python program to convert into decimal number system
# from sqlite3 import Binary


# n1 = 0o17
# n2 = 0B1110010
# n3 = 0X1c2

# n = int(n1)
# print('Octal 17 = ' , n)
# n = int(n2)
# print('Binary 1110010 = ', n)
# n = int(n3)
# print('Hexadecimal 1c2 = ', n)



## OR
s1 = "17"
s2 = "1110010"
s3 = "1c2"

n = int(s1, 8)
print('Octal 17 = ' , n)
n = int(s2, 2)
print('Binary 1110010 = ', n)
n = int(s3, 16)
print('Hexadecimal 1c2 = ', n)