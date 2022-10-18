# Python program to check if the number is a Palindrome number or not
# take input from the user

Number = int(input("\nEnter number to check whether it's Palindrome or Not: "))
temp = Number  # Assigning NUmber to temp
pal = 0   # Initialize Pal

while temp > 0:  # While condition to check whether the number is greater than 0 or not

    dig = temp % 10
    pal = pal * 10 + dig
    temp = temp // 10

if Number == pal:      # Checking whether it's Palindrome or not
    print("\nThe number", Number, "is a palindrome")

else:
    print("\nThe number", Number, "is not a palindrome")
