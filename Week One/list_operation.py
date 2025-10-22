favorite_foods = ["Pizza", "Biryani", "Pasta", "Burger", "Ice Cream"]
print(favorite_foods)
#accessing using index
print(favorite_foods[4])

#using negative index
print(favorite_foods[-2])

#using slicing
print(favorite_foods[2:5])

#modify item
favorite_foods[2] = "Meggie"
print(favorite_foods)

#adding new item

favorite_foods.append("Butter Chicken")
print(favorite_foods)