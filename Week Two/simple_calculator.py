print("Wellcome to Simple Calculator")

num1 = float(input("Enter the first number: "))
operator = input("Please select the desire operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    rerult =  num1+num2
elif operator == '-':
    rerult =  num1-num2
elif operator == '*':
    rerult =  num1*num2
elif operator == '/':
    if(num2 == 0):
        print("Division will not happen with zero")
    else:
        rerult =  num1+num2    
print("Result: ",rerult)
