
import sys

def whatis(object: any) -> int:
	if isinstance(object, int) and object %2 == 0:
		print("I'm Even.")
	elif isinstance(object, int) and object%2 != 0:
		print("I'm Odd.")

if len(sys.argv) == 2:
	try:
		res = int(sys.argv[1])
		whatis(res)
	except AssertionError as e:
		assert False,"argument is not an integer"		
elif len(sys.argv) > 2:
	try:
		assert False, "more than one argument is provided"
	except AssertionError as e:
		print(f"AssertionError: {e}")