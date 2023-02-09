number_string = input()
number = int(number_string)

upper = number + 1
lower = number - 1

while lower > 0 and upper <= 10 ** 15:
	is_upper_alien = True
	is_lower_alien = True

	for char in number_string:
		if char in str(upper):
			is_upper_alien = False

		if char in str(lower):
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

	upper += 1
	lower -= 1
