# Python Project
# Mini Project CALCULATOR      
                               
first=input("Enter first number : ")
operator = input("Enter operator(+,_,*,/,%) : ")
second=input("Enter second number : ")
                               
first=int(first)               
second=int(second)           

if operator == "+":            
    print(first + second)      
elif operator == "-":          
    print(first - second)      
elif operator == "*":          
    print(first * second)      
elif operator == "/":          
    print(first / second)      
elif operator == "%":          
    print(first % second)      
else:                          
    print("Invalid Operation.")
