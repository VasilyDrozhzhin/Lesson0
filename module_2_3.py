my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while len(my_list) > 0:
	i = my_list.pop(0)
	if i < 0:
		break
	elif i == 0:
		continue
	else:
		print(i)
