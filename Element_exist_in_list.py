# Python program to check element is present in list or not

# Driver mode(Main function)
List = []  # creating a new list
Num = int(input("Enter the number of list needed : "))  # Getting a user input of how much number of list is needed

for i in range(Num):  # Loop to get an input from user
    print("Enter the value for Index", i)
    List1 = int(input())  # Variable to save an input given by user

    List.append(List1)  # Using an inbuilt function to append the input given by user to first List

print("\nThe given list by user is: ", List)  # Printing the list
Element_to_check = int(input("Enter the element to check in list: ")) # Getting a user input to check
count = List.count(Element_to_check)  # Checking whether the element is available in list or not

if count > 0:  # Condition to check whether the element is existed or not
    print("\nThe element", Element_to_check, "is present in list")
else:
    print("\nThe element", Element_to_check, "is not present in list")


