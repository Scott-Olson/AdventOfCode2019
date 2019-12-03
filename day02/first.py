stream = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]
stream[1] = 12
stream[2] = 2

test1 = [1,0,0,0,99] #2,0,0,0,99
test2 = [2,3,0,3,99] #2,3,0,6,99
test3 = [2,4,4,5,99,0] #2,4,4,5,99,9801
test4 = [1,1,1,4,99,5,6,0,99] #30,1,1,4,2,5,6,0,99

def decode(streamIn: list):
	stream = streamIn
	print(stream)
	for i in range(0, len(stream), 4):

		first = i + 1
		second = i + 2
		res_loc = i + 3

		# addition
		if stream[i] == 1:
			print("addition hit: %i" % i)
			print("altering %i location with: %i" % (stream[stream[res_loc]], stream[stream[first]] + stream[stream[second]]))
			stream[stream[res_loc]] = stream[stream[first]] + stream[stream[second]]

		# multiplication
		elif stream[i] == 2:
			print("multiplication hit: %i" % i)
			print("altering %i location with: %i + %i" % (stream[stream[res_loc]], stream[stream[first]], stream[stream[second]]))
			stream[stream[res_loc]] = stream[stream[first]] * stream[stream[second]]

		# terminal code
		elif stream[i] == 99:
			# end program
			print("Program state restored: %i" % stream[0])
			return stream[0]

print(decode(stream))

# decode(stream)
# previous attempts: 1, 113(too low), 2842646(too low), 2842648 correct
