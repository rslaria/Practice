list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = []
list_3 = ["A", "B", "C"]
list_4 = [1, 2, 3, 2, 4, 5, 4, 6, 7, 6, 8, 9]


# Check, count, and print the contents of each list

if len(list_1) == 0:
    print("List_1 is empty")
else:
    print("list_1 is not empty")
    print("The length of list_1 is:", len(list_1))
    print("list_1:", list_1)

print()  # Add an empty line

if len(list_2) == 0:
    print("List_2 is empty")
else:
    print("list_2 is not empty")
    print("The length of list_2 is:", len(list_2))
    print("list_2:", list_2)


print()  # Add an empty line

if len(list_3) == 0:
    print("List_3 is empty")
else:
    print("list_3 is not empty")
    print("list_3:", list_3)
    print("length of list_3 is:", len(list_3))

print()  # Add an empty line

# Remove Duplicate from the List

unique_list = list(set(list_4))
print("list_4:",unique_list)

