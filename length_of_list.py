# Python program to find the length of an list
List = [12, 34, 56, 78, 34, 23]    # Input list

print("\nLength of an list using Inbuilt function: ", len(List))   # Finding length using Inbuilt function

# For loop to Find length without using Inbuilt function

count = 0
for i in List:
    count = count + 1

print("\nLength of an list without using Inbuilt function: ", count)
