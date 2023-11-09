def map(function, list_):
	if len(list_) == 0:
		return []

	return [function(list_[0])] + map(function, list_[1:])

print(map(lambda x: x * 2, [1, 2, 3]))

def filter(function, list):
	# Return a new list of all the elements in list_ that pass
	# function
	pass

filter(lambda x: x < 5, [1, 27, 13, 4, 3]) == [1, 4, 3]
