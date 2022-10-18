# Bubble sorting Algorithm

Lists = [1, 0, 9, 32, 7, 8, 12, 885, 35, 90, 99, 123]
print("\nBefore sorting the list is  : ", Lists)    # List before sorting

for i in range(len(Lists)-1, 0, -1):  # Start and Step is optional
    for j in range(i):                # Start and Step is optional
        if Lists[j] > Lists[j + 1]:  # Condition to check whether the previous number is greater than the current number
            swap = Lists[j]             # If the current number is greater storing the number in temp variable
            Lists[j] = Lists[j + 1]       # Swapping the current value and previous value
            Lists[j + 1] = swap         # Swapping the current value and previous value

print("\nAfter sorting the output is : ", Lists)     # List after sorting
