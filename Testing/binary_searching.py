"""Binary Search"""
search_key = "Brutus the Gruesome\n"
with open("super_villains_list.txt") as file:
    villains = file.readlines()

lower_bound, upper_bound = 0, len(villains) - 1
middle = (lower_bound + upper_bound) // 2
found = False

while lower_bound <= upper_bound and not found:
    middle = (lower_bound + upper_bound) // 2

    if villains[middle] < search_key:
        lower_bound = middle + 1
    elif villains[middle] > search_key:
        upper_bound = middle - 1
    else:
        found = True

if found:
    print("Villain name is at position", middle)
else:
    print("Villain name not found.")
