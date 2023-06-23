import math as m

total_area = 0.0
#Ask user to continue
def prompt():
	while True:
		prompt = input("Enter another shape (y/n): ").lower()
		if prompt == "y":
			return True
		elif prompt =="n":
			return False
		else: ##whoops
			continue

while True:
	input_shape = input("Type of shape (circle, rectangle, or triangle): ").lower()
	if input_shape == "circle":
		radius = float(input("Radius: "))
		total_area += float(m.pi*radius**2)
	elif input_shape == "rectangle":
		r_length = float(input("length: "))
		r_height = float(input("Height: "))
		total_area += r_length*r_height
	elif input_shape == "triangle":
		t_base = float(input("Base: "))
		t_height = float(input("height: "))
		total_area += (t_base*t_height)/2
	else: ##whoops
		continue
	#Ask user to continue
	if prompt():
		continue
	else: ##exit
		break
print("The total area is "+str(total_area))

