import euler1, euler2, euler3, euler5

def test_euler1():
	assert euler1.result() == 233168

def test_euler2():
	assert euler2.result() == 4613732

def test_largest_prime_factor_small():
	assert euler3.largest_prime_factor_of(13195) == 29

def test_largest_prime_factor_large():
	assert euler3.largest_prime_factor_of(600851475143) == 6857

def test_smallest_multiple():
	assert euler5.smallest_number_evenly_divisble_by_all_integers_up_to(10) == 2520

def test_smallest_multiple(): # this test runs slow - 29s
	assert euler5.smallest_number_evenly_divisble_by_all_integers_up_to(20) == 232792560

