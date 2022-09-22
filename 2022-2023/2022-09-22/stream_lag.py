n = int(input())

max_delay = 0

for _ in range(n):
	time, packet = map(int, input().split()) # E.g. 1, 2

	delay = time - packet

	max_delay = max(max_delay, delay)

print(max_delay)
