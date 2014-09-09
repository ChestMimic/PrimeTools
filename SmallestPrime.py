#Returns the smallest prime number in num
def SmallestPrime(num):
	if num == 0:
		return 0
	elif num < 0:
		return -1
	else:
		i = 2
		while i < num:
			if num%i == 0:
				break
			i += 1
	return i