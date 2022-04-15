
lst = ["Adam", "Jacob", "Mike", 25, False]  # List can store any data type and any no of element
    #    0        1       2      3    4      Stores using index
lst[0] = "Amaan"  # Get the particular index value and change
print(lst)
print(lst[2])  # Print Which ever index value we give.
print(lst[-1])  # Print reverse
print(lst[2:])  # If you want to print a value after certain index then it will print like this
print(lst[2:4])  # If you want to print particular index

lucky_numbers = [2, 4, 8, 16, 32, 64, 128]
frnds = ["Alpha", "Beta", "Ghama", "Mike", "Johnson", "Zaid"]
frnds.append("Zakir") # Add the new name into the frnds list.
frnds.extend(lucky_numbers) # Add Lucky_numbers list ro frnds list and print
print(frnds) # print Both the list together.
frnds.insert(1, "Alphabets") # Insert new word in the index 1 and print
print(frnds)
frnds.remove("Alpha") # Remove the particular word from the given list
print(frnds)
frnds.pop() # Pop delete the last element from the list
print(frnds)
print(frnds.index("Zaid")) # Search for particular element in the list and print the index no
frnds.clear() # Clear the List
print(frnds)

