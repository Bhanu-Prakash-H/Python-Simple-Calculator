# int1 = int(input('enter num1 : '))
# int2 = int(input('enter num2 : '))
# print('add = 1, sub = 2, mul = 3, div = 4')
# option = int(input('Choose any one option : '))
# if option == 1:
#     print(int1 + int2)
# elif option == 2:
#     print(int1 - int2)
# elif option == 3:
#     print(int1 * int2)
# elif option == 4:
#     print(int1 // int2)
# else:
#     print('Choose Valid Option')


''' Program to make simple calculator '''
'''Define functions'''
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul (x,y):
    return x * y
def div(x,y):
    return x // y

'''Take input from User'''
x = int(input('enter num1 : '))
y = int(input('enter num2 : '))
print('Choose 1/2/3/4 to add/sub/mul/div')
option = int(input('Enter choice 1/2/3/4: '))

if option == 1:
    print(add(x,y))
elif option == 2:
    print(sub(x,y))
elif option == 3:
    print(mul(x,y))
elif option == 4:
    print(div(x,y))
else:
    print('Choose Valid Option')










