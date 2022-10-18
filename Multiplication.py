number = int(input("\nEnter the Multiplication table you need : "))
number1 = int(input("\nEnter the number of columns to print : "))

for i in range(1, number1 + 1):
    print(number, "x", i, "=", number * i)  # To print the Multiplication table

else:
    print("\nThe multiplication table for table", number, "th table is completed")  # To show the Loop completion
