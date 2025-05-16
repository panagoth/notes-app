while True:
    print("Welcome to Notes App!")
    print("1. Add note")
    print("2. View notes")
    print("3. Delete note")
    print("4. Exit")
    choice = int(input("What is your choice?: "))

    if choice == 1:
        note = input("Enter your note: ")
        with open("notes.txt", "a") as file:
            file.write(note +"\n")
    elif choice == 2:
        with open("notes.txt", "r") as file:
            contents = file.read()
            print(contents)
    elif choice == 3:
        with open("notes.txt") as file:
            read_notes = file.readlines()
            for i, line in enumerate(read_notes):
                print(f"{i}: {line.strip()}")
        to_delete = int(input("Enter the number of the note to delete: "))
        del read_notes[to_delete]
        with open("notes.txt", "w") as file:
            file.writelines(read_notes)
            print(f"The note #{to_delete} has been removed.")
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Please enter a valid option.")

    again = input("Would you like to choose an other option?(Y/N): ").upper()
    if again != "Y":
        print("Exiting program. Goodbye!")
        break

