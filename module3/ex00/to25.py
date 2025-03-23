#!/usr/bin/python3

num = input("Enter number less than 25...\n")
if int(num) > 25:
    print("Error")
n = int(num)
while n <= 25:
    print("Inside the loop, number is", n)
    n += 1
