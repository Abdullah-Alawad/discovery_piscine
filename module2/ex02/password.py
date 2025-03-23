#!/usr/bin/python3
passw = input("Enter Password... ")
password = "VERY STRONG PASSWORD"
pas = passw.strip()
if pas == password:
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED")
