#!/usr/bin/env python

order_str, capacity_str = input().split()
order = int(order_str)
capacity = int(order_str)

water = capacity

refills = 0

for _ in range(order):
	line = input()

	if line[-1] == "L":
		amount = int(line[:-1]) + 1
	else:
		amount = int(line)

	if water < amount:
		refills += 1

		water = capacity

	water -= amount

print(refills)
