# interestingsolution inspired by reddit user

def check(n):
	# first conditional checks to see if the input is in fact sorted; means that the solution is only increasing
	# second conditional checks that the input has a grouping of exactly 2 of the same digits
    return list(n) == sorted(n) and 2 in map(n.count, n)

print(sum(check(str(n)) for n in range(254032, 789860 + 1)))