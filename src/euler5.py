# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_number_evenly_divisble_by_all_integers_up_to(number):
	# must be a multiple of 20
	candidate = number
	while 1 :
		divisble_by_all_integers_in_number = True
		for i in range(1, number):
			if (candidate % i != 0):
				divisble_by_all_integers_in_number = False
		if (divisble_by_all_integers_in_number):
			return candidate
		# the candidate must be divisble by number, so only check candidates which are divisible by number
		candidate = candidate + number	
