#!/usr/bin/python3

num1 = input("Enter first number... ")
num2 = input("Enter second number... ")
mult = int(num1) * int(num2)
print(num1, "x", num2, "=", mult)
if mult > 0:
    print("The result is positive.")
elif mult < 0:
    print("The result is negative")
else:
    print("The result is ZERO")