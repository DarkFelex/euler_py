import euler1, euler2, euler3, euler5, euler6, euler9

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

# def test_smallest_multiple(): # this test runs slow - 29s
	# assert euler5.smallest_number_evenly_divisble_by_all_integers_up_to(20) == 232792560

def test_sum_square_difference():
	assert euler6.sum_square_difference_of_numbers_below(10) == 2640

def test_sum_square_difference():
	assert euler6.sum_square_difference_of_numbers_below(100) == 25164150

def test_pythagorean_triplet():
	product_of_a_b_c = 60
	assert euler9.pythagorean_triplet_adds_up_to(12) == product_of_a_b_c

# def test_pythagorean_triplet(): # test runs slow - 19s
	# assert euler9.pythagorean_triplet_adds_up_to(1000) == 31875000

