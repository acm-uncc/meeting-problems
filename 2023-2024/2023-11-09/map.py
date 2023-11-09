def map_increment(numbers):
	return map(lambda x: x + 1, numbers)

def for_increment(numbers):
	result = []

	for i in range(len(numbers)):
		result.append(numbers[i] + 1)

	return result

for number in map_increment([1, 3, 12, 17, 52, 42]):
	print(number)
