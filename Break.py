# Example program for Break statement
# take input from the user

Number = int(input("\nEnter any number : "))
print("\nThe output is : ")

for i in range(1, Number):   # Used to check the number
    if i % 9 == 0:           # Used to check does the number has the multiples of 9
        break                # Used for break if the given number has multiples of 9
    print(i, end="  ")        # Used to print
print("\n")                  # Used to print new line
