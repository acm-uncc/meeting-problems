import math

car1_pos, car2_pos = map(int, input().split())

car1_times = list(map(int, input().split()[1:]))
car2_times = list(map(int, input().split()[1:]))

sorted_times = sorted(list(set(car1_times + car2_times)))

if car1_pos < car2_pos:
	car1_pos += 4.4
else:
	car1_pos, car2_pos = car2_pos + 4.4, car1_pos
	car1_times, car2_times = car2_times, car1_times

positions1 = [None] * len(sorted_times)
positions2 = [None] * len(sorted_times)
velocities1 = [None] * len(sorted_times)
velocities2 = [None] * len(sorted_times)

if len(positions1) > 0:
	positions1[0] = car1_pos

if len(positions2) > 0:
	positions2[0] = car2_pos

for times, positions, velocities in [
	(car1_times, positions1, velocities1),
	(car2_times, positions2, velocities2)
]:
	i = 0

	for j in range(len(sorted_times)):
		if i < len(times) and sorted_times[j] == times[i]:
			if j == 0:
				velocities[j] = 1
			else:
				velocities[j] = 1 - velocities[j - 1]

			i += 1
		elif j == 0:
			velocities[j] = 0
		else:
			velocities[j] = velocities[j - 1]

		if j < len(sorted_times) - 1:
			positions[j + 1] = \
				positions[j] + velocities[j] * (sorted_times[j + 1] - sorted_times[j])

sorted_times.append(math.inf)

for i in range(len(sorted_times) - 1):
	if velocities1[i] != velocities2[i]:
		collision_time = \
			(positions2[i] - positions1[i]) / (velocities1[i] - velocities2[i])

		if 0 <= collision_time <= sorted_times[i + 1] - sorted_times[i]:
			print(f"bumper tap at time {math.ceil(sorted_times[i] + collision_time)}")

			break
else:
	print("safe and sound")
