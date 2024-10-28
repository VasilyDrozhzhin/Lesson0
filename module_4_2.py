def test_function():
	def inner_function():
		print('Я в области видимости функции test_function')

	inner_function()
	global a
	a = inner_function


test_function()
a()
