def add(a, b):
    return a + b

def sub(a, b):
    return a - b

num1 = int(input("first number: "))
num2 = int(input("second number: "))

op = int(input("input 1 to add and 2 to subtract: "))

if op == 1:
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif op == 2:
    print(f"{num1} - {num2} = {sub(num1, num2)}")
else: 
    print("wrong number :(")