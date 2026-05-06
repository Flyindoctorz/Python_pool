
def all_thing_is_obj(object: any) -> int:
	types = type(object)
	if isinstance(object, list):
		print(f"List : {types}")
	elif isinstance(object, tuple):
		print(f"Tuple : {types}")
	elif isinstance(object, set):
		print(f"Set : {types}")
	elif isinstance(object, dict):
		print(f"Dict : {types}")
	elif	isinstance(object, str):
		print(f"{object} is in the kitchen : {types}")
	else:
		print("Type not found")
	return 42


