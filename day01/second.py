lines = open('input.txt').read().split('\n')

# test cases
test1 = 0
fuel_in = 1969
fuel_val = fuel_in
while fuel_val > 2:
	fuel_val = (fuel_val // 3) - 2
	print(fuel_val)
	if fuel_val > 0:
		test1 += fuel_val

print("test 1, expected: 966 actual: %i" % test1)
# passed

test2 = 0
fuel_in = 100756
fuel_val = fuel_in
while fuel_val > 2:
	fuel_val = (fuel_val // 3) - 2
	print(fuel_val)
	if fuel_val > 0:
		test2 += fuel_val
print("test 2, expected: 50346 actual: %i" % test2)
# passed


# ATTEMPT
fuel_needed = 0

for line in lines:
	fuel_val = int(line)
	while fuel_val > 2:
		fuel_val = (fuel_val // 3) - 2
		if fuel_val > 0:
			fuel_needed += fuel_val

print("Total fuel needed: %i" % fuel_needed)
# first try output: 4770725 CORRECT

# switch the solution to recursion

def fuel_calc(fuel_val: int, c_fuel: int):
	fuel_val = fuel_val // 3 - 2
	if fuel_val > 0:
		print("in the rec loop")
		print("current stats: %i  %i" % (fuel_val, c_fuel))
		return fuel_calc(fuel_val, c_fuel + fuel_val)
	return c_fuel

sum_fuel = 0
for line in lines: 
	sum_fuel += fuel_calc(int(line), 0)

print("Recursion test formula. Expected: 4770725, actual: %i" % sum_fuel)
