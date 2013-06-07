# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pythagorean_triplet_adds_up_to(number):
	for a in range(1, number -1):
		for b in range(1, number -1):
			for c in range(1, number -1):
				if ((a + b + c == number) and (a * a + b * b == c * c)):
					return a * b * c

