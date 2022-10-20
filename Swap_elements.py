# Python program to swap two elements

mylist = []   # Creating a new list
Num = int(input("Enter the number of list needed: "))   # Getting a user input of how much number of list is needed
for i in range(Num):    # Loop to get an input from user
    print("Enter the value for index", i)
    List1 = int(input())     # Variable to save an input given by user

    mylist.append(List1)     # Using an inbuilt function to append the input given by user to first List
print("The user given list is: ", mylist)     # Printing the list

posOne = int(input("Enter the first position to swap: "))     # Getting a user input of which position need to swap
posTwo = int(input("Enter the second position to swap: "))    # Getting a user input of which position need to swap

if (posOne and posTwo) <= len(mylist):      # Condition to check whether the position is available or not
    posOneElement = mylist[posOne - 1]      # Storing the first position element to new variable
    posTwoElement = mylist[posTwo - 1]      # Storing the second position element to new variable

    mylist[posOne - 1] = posTwoElement      # Inserting the swapped element
    mylist[posTwo - 1] = posOneElement      # Inserting the swapped element

    print("List after swapping the number is: ", mylist)   # Printing the list after the swap

else:    # Condition to check whether the position is available or not
    print("\nThe position entered is not available in List")   # Printing the statement of unavailability of position

