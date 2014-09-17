def isPrime(num):
	#a brute force attempt to determine if a number is prime
	#basically divide by each number from 2 to num-1. If at any point num%div = 0, return false, else true
	#additionally, this function assumes that negative numbers and 0 are not prime.
	#Mathematically, the loop should also allow 1 to comfirm as a prime number, since it will skip the loop to the return True statement
	#Efficiency is probably around worst O(num)
	
	if  num < 1:
		return False
	i = 2
	while i < num-1:
		if num%i == 0:
			return False
		i += 1
	return True

if __name__ == '__main__':
	count = -3
	while count <= 13:
		r = isPrime(count)
		print(repr(count) + " is prime: " + repr(r))
		count += 1
		
