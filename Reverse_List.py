List = []  # creating a new list
Num = int(input("Enter the number of list needed : "))  # Getting a user input of how much number of list is needed

for i in range(Num):  # Loop to get an input from user
    print("Enter the value for Index", i)
    List1 = int(input())  # Variable to save an input given by user

    List.append(List1)  # Using an inbuilt function to append the input given by user to first List

print("\nThe given list by user is  : ", List)  # Printing the list before reverse

List.reverse()                                  # Inbuilt function to reverse a list
print("The list after reversal is : ", List)    # Printing the list after reversal
