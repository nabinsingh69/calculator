print("SIMPLE CALCULATOR")
print("enter the operation to perform")
print("""
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    """)
operation = int(input("select from the above operations: "))

if operation == 1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum =num1+num2
    print("The Addition of two numbers is: ",sum)
elif operation == 2:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sub =num1-num2
    print("The Subtraction of two numbers is: ",sub)
elif operation == 3:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    mul =num1*num2
    print("The Multiplication of two numbers is: ",mul)
elif operation == 4:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    diff =num1/num2
    print("The Division of two numbers is: ",diff)
else:
    print("Choose from the above operations")

