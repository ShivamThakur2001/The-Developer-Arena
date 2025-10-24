def areaOfRectangle(lenght, width):
    area = lenght*width
    return area

length = float(input("Enter the lenght of rectangle: "))
width = float(input("Enter the width of rectangle: "))

print("Area of rectangle is: ",areaOfRectangle(length,width))