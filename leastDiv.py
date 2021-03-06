# Francis Adepoju, 2018-02-14		Ex. #4
""" The smallest positive number that is evenly divisible by all of the numbers from 1 to 20... Euler problem 5
 
 ... https://www.w3resource.com/euler-project/euler-problem5.php#
 Given that 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 
 The number in question must be divisible by all of the numbers between 1 and 20 (assume inclusive for the ranges).
 As a result, it must be divisible by all of the numbers between 1 and 10. The smallest number that is divisible
 by all the numbers between 1 and 10 (given by Project Euler) is 2520. Thus, the number in question here must be a
 multiple of 2520.

 The program to find this number will start at 2, iterate to 20, and for each of those numbers it will divide by every 
 known prime less than that number (technically any prime less than the square root of the number) to determine their factorization. 
 We will find the numbers that are prime as we go (they won't be divisible by any lesser prime, by definition).
"""
# Define the function to Compute the greatest common denominator (gcd)
def gcd(x, y):    
  	# return (y and gcd(y, x % y) or x)	 # This inline imlementation also works
	while x != 0 and y != 0:
		if x > y:
			x = x % y
		else:
			y = y % x

	if x == 0:
		return y
	else: 
		return x		
# Define the Function to compute the lcm of two numbers
def lcm(x, y):
	return (x * y / gcd(x, y))

# Find the least common multiple of 1 & 20, recursively
smallestInteger = 1
for i in range(1, 21):     
	smallestInteger = lcm(smallestInteger, i)
	print("factor found :", int(smallestInteger)) 
print("Euclidean Algorithm Implementation yields: ", int(smallestInteger))
print("")
# More test
print (f'TEST: The gcd of 221 and 323 is {gcd(221, 323)}')

