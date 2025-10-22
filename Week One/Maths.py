while(True):
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n\nEnter your operation:")
    num = int(input())
    if(num >4 or num<1):
        break
    else: 
        a ,b = int(input("Enter first value: ")), int(input("Enter second value: "))
   
        if(num == 1):
            print(f"\nAddition of first and second value is: {a+b}")
        
        elif(num == 2):
            print(f"\nSubtraction of first and second value is: {a-b}")
        
        elif(num == 3):
            print(f"\nMultiplication of first and second value is: {a*b}")
        
        elif(num == 4):
            print(f"\nDivision of first and second value is: {a/b}")
        
        else:
            break

    
