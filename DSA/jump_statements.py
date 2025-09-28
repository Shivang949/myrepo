# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     temp = i
#     while temp%2 == 0:
#         temp /= 2
#     if temp != 1:
#         continue
#     print(i)


limit = 10
num = int(input("Enter a number: "))
i = 0
sum = 0
while i<= num:
    sum += i
    i += 1
    if i >=limit:
        break
print("Sum is:", sum)