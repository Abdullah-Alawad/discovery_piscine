#!/usr/bin/python3

outer_num  = 0
while outer_num <= 10:
	inner_num = 0
	print("Table of", outer_num, ":", end=" ")
	while inner_num <= 10:
		print(inner_num*outer_num, end=" ")
		inner_num += 1
	print("")
	outer_num += 1

