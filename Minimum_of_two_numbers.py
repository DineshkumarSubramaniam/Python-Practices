# Python program to find maximum among 2 numbers
number1 = int(input("\nEnter the first number: "))  # User input of number 1
number2 = int(input("Enter the second number: "))  # User input of number 2

if number1 < number2:     # checking whether first number is less than second number or not
    print("OUTPUT : Number1", number1, "is lesser than Number2", number2)

elif number2 < number1:   # checking whether second number is less than first number or not
    print("OUTPUT : Number2", number2, "is lesser than Number1", number1)

else:                     # Condition to check whether both numbers are equal or not
    print("OUTPUT : Both the numbers are equal")
