# Need to write a code which takes two inputs(n, m) and prints a pattern of n rows and m columns.
# For example, if n = 3 and m = 5, then the output should be:
# o*o*o
# *o*o*
# o*o*o


# n = int(input("Enter number of rows: "))
# m = int(input("Enter number of columns: "))
# for i in range(n):
#     for j in range(m):
#         print(j+1, end=" ")
#     print(" ")


n = 5

# Right angle triangle

for i in range(1,n+1):
    for j in range(1, i+1):
        print('*', end=" ")
    print(" ")

# Inverse right angle triangle

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print('*', end=" ")
    print(" ")

# pyramid pattern


    

