def main():
    """Searching for 'search_key' in the villains list."""
    search_key = "Uwu the Degenerate"

    with open("super_villains_list.txt") as file:
        villains = file.readlines()

    name_found = False
    for villain in villains:
        if villain == search_key:
            print("The villain", search_key.rstrip(),  # Strip for printing.
                  "is located at line", villains.index(villain),
                  "in the list of villains.")

            name_found = True
            break

    if name_found is False:
        print(search_key, "was not found in the list of villains.")


main()
