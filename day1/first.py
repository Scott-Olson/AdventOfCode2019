lines = open('input.txt').read().split('\n')


fuel_needed = 0

# test case
test1 = (1969 // 3) - 2 
print("test 1, expected: 654 actual: %i" % test1)

test2 = (100756 // 3) - 2
print("test 2, expected: 33583 actual: %i" % test2)

for line in lines:
	fuel_needed += (int(line) // 3) - 2

# returned result: 3182375 correct!

print("Total fuel needed: %i" % fuel_needed)