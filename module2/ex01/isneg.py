#!/usr/bin/python3

print("Enter a number...", end=" ")
x = input()
if int(x) < 0:
    print("This number is negative.")
elif int(x) > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")
