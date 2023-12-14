import math

height = int(input("Enter wall height: "))
width = int(input("Enter wall width: "))

def cansRequired(height,width):
    area = width * height
    coverage=5
    cans_required = math.ceil(area / coverage)
    print(cans_required)

cansRequired(height,width)