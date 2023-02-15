number_string = input()
number = int(number_string)

upper = number + 1
lower = number - 1

while lower > 0 and upper <= 10 ** 15:
	lower_str = str(lower)
	upper_str = str(upper)

	is_upper_alien = True
	is_lower_alien = True

	for char in number_string:
		if char in upper_str:
			is_upper_alien = False

		if char in lower_str:
			is_lower_alien = False

		if not is_upper_alien and not is_lower_alien:
			break

	if is_upper_alien or is_lower_alien:
		if is_upper_alien and not is_lower_alien:
			print(upper)
		elif is_lower_alien and not is_upper_alien:
			print(lower)
		elif is_upper_alien and is_lower_alien:
			print(f"{lower} {upper}")

		break

	lower_power = None

	for i in range(len(lower_str) - 1, -1, -1):
		if lower_str[i] in number_string:
			lower_power = 10 ** (len(lower_str) - i - 1)

			break

	upper_power = None

	for i in range(len(upper_str) - 1, -1, -1):
		if upper_str[i] in number_string:
			upper_power = 10 ** (len(upper_str) - i - 1)

			break

	power = min(lower_power, upper_power)

	lower_distance = lower % power + 1
	upper_distance = power - upper % power

	distance = min(lower_distance, upper_distance)

	lower -= distance
	upper += distance
else:
	print("Impossible")
