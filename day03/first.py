A,B = open('input.txt').read().split('\n')
A,B = [x.split(',') for x in [A,B]]


dx = {'U': 0 , 'D': 0, 'L': -1, 'R': 1}
dy = {'U': 1 , 'D': -1, 'L': 0, 'R': 0}


# instead of recording just the end points, record the entire path step by step.
# this will allow for the intersection detection later
# hints from others, use a set


# part 2 is about which has fewest steps to intersections
def wire_path(wire: list):
	x = 0
	y = 0
	length = 0
	ans = {}

	for cmd in wire:
		d = cmd[0]
		n = int(cmd[1:])
		for step in range(n):
			x += dx[d]
			y += dy[d]
			length += 1
			if (x,y) not in ans:
				ans[(x,y)] = length

	return ans


loc_a = wire_path(A)
loc_b = wire_path(B)

both = set(loc_a.keys())&set(loc_b.keys())
part1 = min([abs(x) + abs(y) for (x,y) in both])
part2 = min([loc_a[p] + loc_b[p] for p in both])
print(part1, part2)
