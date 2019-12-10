# puzzle entry 254032-789860

def val_num(val_in: int):
	adj_dig = False
	str_val = str(val_in)

	for i in range(1, len(str_val)):
		if int(str_val[i]) < int(str_val[i - 1]):
			return False

		if int(str_val[i]) == int(str_val[i - 1]):
			adj_dig = True

		if i == (len(str_val) -1) and adj_dig == True:
			return True

	return False

print(val_num(111111))
print(val_num(223450))
print(val_num(123789))

solutions = []
for i in range(254032, 789860 + 1):
	if val_num(i):
		print('Solution found at: ', i)
		solutions.append(i)
print(len(solutions))
