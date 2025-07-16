
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns in each row
    for col in range(size):
        print("*", end="")  # Print stars side by side
    print()  # Move to next line after each row
    row += 1  # Move to the next row
