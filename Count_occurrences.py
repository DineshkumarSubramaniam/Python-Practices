# Main function
# Python program to check the occurrences of an individual numbers

List = []    # Creating a list

number = int(input("Enter the number of list needed: "))   # Getting a user input of how much number of list is needed
for i in range(number):   # Loop to get an input from user
    print("Enter the value for index", i)
    List1 = int(input())  # Variable to save an input given by user

    List.append(List1)    # Using an inbuilt function to append the input given by user to first List
print("\nThe list given by user is: ", List)   # Printing the list

occurrences_to_check = int(input("\nEnter the number to check the occurrences: "))    # Checking whether the element
# is available in list or not

count1 = 0    # Initializing a variable
for i in List:   # Condition to check whether the element is occurring in list or not
    if i == occurrences_to_check:
        count1 = count1 + 1
print("\nThe number", occurrences_to_check, "is Present", count1, "time in this List")

