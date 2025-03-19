def get_suum_even(number):
	add = 0	
	for count in number:
		if count % 2 == 0:
			add += count
	return add

def get_prime_number(number):
	factors = 0
	for count in number:
		if number % count == 0:
			factors+=1
		
		if factors == 2:
			return true
		else:
			return false

	