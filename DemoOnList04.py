
lst = ["Adam", "Jacob", "Mike", 25, False]  # List can store any data type and any no of element
    #    0        1       2      3    4      Stores using index
lst[0] = "Amaan"  # Get the particular index value and change
print(lst)
print(lst[2])  # Print Which ever index value we give.
print(lst[-1])  # Print reverse
print(lst[2:])  # If you want to print a value after certain index then it will print like this
print(lst[2:4])  # If you want to print particular index

lst1_num = [2, 4, 8, 16, 32, 64, 128]
frnds_list = ["Don", "Alpha", "Beta", "Ghama", "Mike", "Johnson", "Zaid", "Zaid"]
frnds_list.sort() # Sort the Friend list in alphabetics
print(frnds_list)
frnds_list.reverse() # Reverse the list order and print
print(frnds_list)
frinds2 = frnds_list.copy() # Copy the frnds_list into frinds2 list. copt from 1 list to other
print(frinds2)
frnds_list.append("Zakir") # Add the new name into the frnds list.
frnds_list.extend(lst1_num) # Add Lucky_numbers list ro frnds list and print
print(frnds_list) # print Both the list together.
print(frnds_list.count("Zaid")) # Count the same element and print the No
frnds_list.insert(1, "Alphabets") # Insert new word in the index 1 and print
print(frnds_list)
frnds_list.remove("Alpha") # Remove the particular word from the given list
print(frnds_list)
frnds_list.pop() # Pop delete the last element from the list
print(frnds_list)
print(frnds_list.index("Zaid")) # Search for particular element in the list and print the index no
frnds_list.clear() # Clear the List
print(frnds_list)

