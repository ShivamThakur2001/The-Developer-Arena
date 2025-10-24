age = int(input("Enter your age:"))

if(age < 0 ):
    age_massege = "Please enter valid age!!"
elif(age <= 12):
    age_massege = "You are a Child, Dream you life"
elif(age <= 19):
    age_massege = "You are a Teenager, Make a good decision"
elif(age <= 35):
    age_massege = "You are a Young Adult, Take your responsibility"
elif(age <= 59):
    age_massege = "You are a Adult, Secure your oldage"
else:
    age_massege = "You are a Senior Citizen, Take care and enjoy"

print(age_massege)