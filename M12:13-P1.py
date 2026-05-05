def display_names(names):
    for name in names:
        print(name)


def display_names_reverse(names):
    index = len(names) - 1
    while index >= 0:
        print(names[index])
        index -= 1


def main():
    last_names = ["Abrham", "Banks", "Cadden", "Davison", "Jacque",
                  "Patel", "Hilton", "Kardashian", "Antison", "Swift"]

    print("Names:")
    display_names(last_names)

    print("\nNames in Reverse:")
    display_names_reverse(last_names)


main()

