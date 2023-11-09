def ball_impact(fuel, calculate_current):
	current_fuel = calculate_current(fuel)

	return current_fuel * current_fuel

print(ball_impact(30, lambda fuel: fuel - 4))
