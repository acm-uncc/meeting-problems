#!/usr/bin/python3.5
import functools

n = [[5,6,7], [3,9,4], [1,8,4,6,8,2], [2]]
result = functools.reduce(lambda c,d: c * d, functools.reduce(lambda a,b: a + b, n))

print("Input:", n)
print("Result:", result)
