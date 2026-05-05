dogs = []

def main():
    menu()

def menu():
    while True:
        print("\n--- Dog Rescue Menu ---")
        print("1. Add a Dog")
        print("2. View Dogs")
        print("3. Find Dog")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addDog()
        elif choice == "2":
            viewDogs()
        elif choice == "3":
            findDog()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def addDog():
    name = input("Enter dog name: ")
    breed = input("Enter dog breed: ")
    age = input("Enter dog age: ")
    weight = input("Enter dog weight: ")

    dog = {
        "name": name,
        "breed": breed,
        "age": age,
        "weight": weight
    }

    dogs.append(dog)
    print("Dog added successfully!")

def viewDogs():
    if len(dogs) == 0:
        print("No dogs available.")
        return

    print("\n--- Dog List ---")
    for dog in dogs:
        print(f"Name: {dog['name']}, Breed: {dog['breed']}, Age: {dog['age']}, Weight: {dog['weight']}")

def findDog():
    search_name = input("Enter dog name to search: ")

    found = False
    for dog in dogs:
        if dog["name"].lower() == search_name.lower():
            print("\nDog Found!")
            print(f"Name: {dog['name']}, Breed: {dog['breed']}, Age: {dog['age']}, Weight: {dog['weight']}")
            found = True
            break

    if not found:
        print("Dog not found.")

main()