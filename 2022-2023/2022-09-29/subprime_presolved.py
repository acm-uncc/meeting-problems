#!/usr/bin/env python

import math

lower, higher = map(int, input().split())

substr = input()

def generate_primes(max_prime):
	is_prime = [True] * (max_prime - 1)

	prime = 2

	while prime * prime <= max_prime:
		if is_prime[prime - 2]:
			for j in range(prime * prime, max_prime + 1, prime):
				is_prime[j - 2] = False

		prime += 1

	return [n for n, n_is_prime in enumerate(is_prime, 2) if n_is_prime]

result = 0

for prime in generate_primes(1299709)[lower - 1:higher]:
	if substr in str(prime):
		result += 1

print(result)
