def ListDivide(numbers,divide = 2):
	x = 0
	for i in numbers:
		if i%divide == 0:
			x += 1
		else:
			continue
	return x
		

def testListDivide():
	class ListDivideException(Exception):
		pass

	if ListDivide([1,2,3,4,5]) != 2:
		raise ListDivideException
	else:
		pass

	if ListDivide([2,4,6,8,10]) != 5:
		raise ListDivideException
	else:
		pass
	
	if ListDivide([30,54,63,98,100], divide = 10) != 2:
		raise ListDivideException
	else:
		pass
	
	if ListDivide([]) != 0:
		raise ListDivideException
	else:
		pass

	if ListDivide([1,2,3,4,5], 1) != 5:
		raise ListDivideException
	else:
		pass

testListDivide()
