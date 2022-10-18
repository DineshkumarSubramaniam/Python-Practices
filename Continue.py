# Example program for Continue statement
# take input from the user

Number = int(input("\nEnter any number : "))
print("\nThe output is : ")

for i in range(1, Number):   # Used to check the number
    if i % 3 == 0:           # Used to skip the multiples of 3
        continue             # Used to continue rather than multiples of 3
    print(i, end="  ")        # Used to print
print("\n")                  # Used to print new line
