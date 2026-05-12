

def NULL_not_found(object: any) -> int:
	types = type(object)
	if object is None:
		print(f"Nothing: {object}{types}")
	elif isinstance(object, float):
		print(f"Cheese: nan {types}")
	elif isinstance(object, int) and not isinstance(object, bool):
		print(f"Zero : {object} {types}")
	elif isinstance(object, str) and not object:
		print(f"Empty: {types}")
	elif isinstance(object, int) and isinstance(object, bool):
		print(f"Fake {types}")
	elif isinstance(object, str) and object:
		print("Type not found")
		return 1
	return 0