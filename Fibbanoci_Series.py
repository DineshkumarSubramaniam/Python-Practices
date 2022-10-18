# Python program to print Fibbanoci series
# take input from the user

Number = int(input("\nEnter the last series to check : "))
print("\nThe fibbanoci series for the given number", Number, "is:")
# initializing variables

num1 = 0
num2 = 1
print(num1)
print(num2)
num3 = num1 + num2
# Using while loop checking the condition

while num3 < Number:

    print(num3)  # Printing the Fibbanoci series
    num1 = num2
    num2 = num3
    num3 = num1 + num2   # Doing the sum operation of the last 2 numbers in Fibbanoci series

else:
    print("\nLoop completed successfully")   # Intimation of whether the loop is successfully completed or not
