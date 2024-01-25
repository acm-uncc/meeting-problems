rows = int(input("Enter Christmas tree height: "))
rows_absolute = abs(rows)

def print_leaves_up_side_down():
	for i in range(rows_absolute - 1, -1, -1):
		inner_spaces = i * 2
		outer_spaces = rows_absolute - i - 1

		if i == rows_absolute - 1:
			filling = "¯"
		else:
			filling = " "

		print(" " * outer_spaces + "\\" + filling * inner_spaces + "/")

def print_leaves_right_side_up():
	for i in range(rows_absolute):
		inner_spaces = i * 2
		outer_spaces = rows_absolute - i - 1

		if i == rows_absolute - 1:
			filling = "_"
		else:
			filling = " "

		print(" " * outer_spaces + "/" + filling * inner_spaces + "\\")

def print_stem():
	column_width = rows_absolute * 2
	step_width = (column_width // 2) - 1

	for _ in range(rows_absolute // 3):
		print(" " * step_width + "||")

if rows < 0:
	print_stem()
	print_leaves_up_side_down()
else:
	print_leaves_right_side_up()
	print_stem()
