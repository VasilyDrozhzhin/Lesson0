numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
	if i == 1:
		continue
	for j in range(2, i):
		if i % j != 0:
			is_prime = True
		else:
			is_prime = False
			break
	if is_prime:
		primes.append(i)
	else:
		not_primes.append(i)
print('Primes: ', primes, '\nNot Primes: ', not_primes)