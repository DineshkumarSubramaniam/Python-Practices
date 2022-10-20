# Python program to Interchange first and last elements

List = []   # creating a new list
Num = int(input("Enter the number of list needed : "))   # Getting a user input of how much number of list is needed

for i in range(Num):  # Loop to get an input from user
    print("Enter the value for Index", i)
    List1 = int(input())     # Variable to save an input given by user

    List.append(List1)       # Using an inbuilt function to append the input given by user to first List

print("\nThe given list by user is: ", List)

temp1 = List.pop(0)             # Deleting the first index element by using pop function
temp2 = List.pop(-1)            # Deleting the last index element by using pop function
print("\nAfter popping the first and last elements the list is :", List)
List.insert(0, temp2)           # Inserting the last index element to first index
List.append(temp1)              # Inserting the first index element to last index
print("\nAfter the interchange of an elements ths list is: ", List)

