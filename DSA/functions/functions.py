# def myFun(num):
#     if(num%2 == 0):
#         print(True)
#     else:
#         print(False)

# myFun(19)

a = int(input('Enter a number a: '))
b = int(input('Enter a number b: '))

# def sumNum(p, q):
#     print("Sum of numbers is:", p+q)

# sumNum(a, b)

# To pass dynamic arguments-> * is used before the argument and its type is tuple so we can iterate inside it to check the total values to be used
def num(*number):
    ans = 0
    for i in number:
        ans += i
    # print(ans)
    return ans

sum1 = num(a,b,49)
sum2 = num(a,b,59)
print(sum1, sum2)

# num(a,b,8)