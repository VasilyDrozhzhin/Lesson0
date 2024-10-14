import random
x = random.randint(3, 20)
result = []
for i in range(1, x):
	for j in  range(i + 1, x):
		if x % (i + j) == 0:
			result.append(i)
			result.append(j)
print('Случайное число: ',x)
print('Пароль: ',*result)

