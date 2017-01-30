# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_difference_of_numbers_below(number):
	squares_sum = 0
	for i in range(1, number +1):
		squares_sum += (i * i)

	number_sum = 0
	for i in range(1, number+1):
		number_sum += i
	square_of_sum = number_sum * number_sum

	return square_of_sum - squares_sum