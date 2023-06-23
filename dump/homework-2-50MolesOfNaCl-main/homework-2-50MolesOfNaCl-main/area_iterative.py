import math as m

num_shapes = int(input("How many shapes? "))
total_area = 0.0

for i in range(0, num_shapes):
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
	else:
		break

print("The total area is "+str(total_area))
