n = int(input("Enter a number: "))
sum = 0
i = 0
n1 = 'o'
n2 = '*'
# for i in range(n+1):
#     sum = sum+i
# print("Sum is:", sum)
# while i<=n:
#     sum = sum+i
#     i = i+1
# print("Sum is:", sum)
# for i in range(n):
#     if(i%2 != 0):
#         print(n2, end="")
#     else:
#         print(n1, end="")

while i<n:
    if(i%2 != 0):
        print(n2, end="")
    else:
        print(n1, end="")
    i = i+1
