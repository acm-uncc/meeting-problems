def generate_primes(max_prime):
	is_prime = [True] * (max_prime - 1)

	prime = 2

	while prime * prime <= max_prime:
		if is_prime[prime - 2]:
			for i in range(prime * prime, max_prime + 1, prime):
				is_prime[i - 2] = False

		prime += 1

	return [i for i in range(2, max_prime + 1) if is_prime[i - 2]]

result = 0

lower, higher = map(int, input().split())

substr = input()

for prime in generate_primes(1299709)[lower - 1:higher]:
	if substr in str(prime):
		result += 1

print(result)
