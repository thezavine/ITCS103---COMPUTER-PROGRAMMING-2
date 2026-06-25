import os

print("\nHello, Welcome to Azeth's Dreams File Manager")

print("\nPlease press ENTER to start...")

while True:
    key = input()

    if key == "":
        break
    else:
        print("Invalid input. Please press ENTER only.")

os.system("cls")

while True:

    print("\n=============================")
    print("     DREAMS FILE MANAGER")
    print("=============================")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")

    ask2 = input("\nEnter your choice: ")

    if ask2 == "":
        print("\nInvalid input. Please enter a choice.")
        continue

    if ask2 == "4":
        print("\n=============================")
        print("      SYSTEM TERMINATED!")
        print("   THANK YOU FOR USING IT. ")
        print("=============================")
        break

    elif ask2 == "1":
        print("\n===================")
        print("     YOUR FILE")
        print("===================\n")

        try:
            with open("Updated_Brandes_dreams.txt", "r") as file:
                content = file.read()

                if content.strip() == "":
                    print("No messages available.")
                else:
                    print(content)

        except FileNotFoundError:
            print("File could not be found.")

    elif ask2 == "2":
        print("\n===========================")
        print("  ADD INSPIRING MESSAGE")
        print("============================\n")

        message = input("Put message: ")

        if message == "":
            print("\nInvalid input. Message cannot be empty.")
            continue

        with open("Updated_Brandes_dreams.txt", "a") as file:
            file.write(message + "\n")

        print("\nMessage added successfully!")

    elif ask2 == "3":
        print("\n===========================")
        print("     REWRITE THE FILE")
        print("===========================\n")

        message = input("Put new message: ")

        if message == "":
            print("\nInvalid input. Message cannot be empty.")
            continue

        confirm = input("\nThis will overwrite the file (y/n): ").lower()

        if confirm == "y":
            with open("Updated_Brandes_dreams.txt", "w") as file:
                file.write(message + "\n")
            print("\nFile overwritten successfully!")

        elif confirm == "n":
            print("\nOperation cancelled.")

        else:
            print("\nInvalid Input")

    else:
        print("\nInvalid choice. Please try again.")