import euler1, euler2, euler3

def test_euler1():
	assert euler1.result() == 233168

def test_euler2():
	assert euler2.result() == 4613732

def test_largest_prime_factor_small():
	assert euler3.largest_prime_factor_of(13195) == 29

def test_largest_prime_factor_large():
	assert euler3.largest_prime_factor_of(600851475143) == 6857