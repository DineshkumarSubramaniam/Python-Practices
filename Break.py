# Example program for Break statement
# take input from the user

Number = int(input("\nEnter any number : "))
print("\nThe output is : ")
# Used to check the number
for i in range(1, Number): 
# Used to check does the number has the multiples of 9
    if i % 9 == 0:  
# Used for break if the given number has multiples of 9
        break    
# Used to print
    print(i, end="  ")   
# Used to print new line
print("\n")                  
