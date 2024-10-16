calls = 0
def count_calls():
	global calls
	calls += 1
def string_info(s):
	l = (len(s), s.upper(), s.lower())
	count_calls()
	return  l
def is_contain(s = '', l = []):
	if s in l:
		x = True
	count_calls()
	return x
print(string_info('urban'))
print(string_info('hello'))
print(is_contain('o', 'hello'))
print(calls)