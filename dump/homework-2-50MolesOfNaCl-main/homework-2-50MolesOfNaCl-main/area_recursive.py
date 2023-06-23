import math as m #pi

num_shapes = int(input("How many shapes? "))

def areaSum(count, sum):
	##exit
	if count <= 0:
		return sum
	else:
		return areaSum(count-1, sum = sum + shapeArea())

def shapeArea():
	shape = input("Type of shape (circle, rectangle, or triangle):")
	if shape == "circle":
		radius = float(input("Radius: "))
		return m.pi*radius**2
	elif shape ==  "rectangle":
		length = float(input("Length: "))
		width = float(input("width: "))
		return length*width
	elif shape == "triangle":
		base = float(input("Base: "))
		height = float(input("height: "))
		return (base*height)/2
	##catch other stuff
	else:
		return 0

print(areaSum(num_shapes, 0.0))
