ListOfNames = []
Index = []
Menu = True

while Menu:
    print("=========================" + "\n"
          "1 - Enter new name" + "\n" +
          "2 - Display list of names" + "\n" +
          "3 - Update name" + "\n" +
          "4 - Delete name" + "\n" +
          "5 - Exit/Stop" + "\n" +
          "=========================" + "\n")
    Menu = input("Choose one from the menu: ")
    if Menu == "1":
        Name = input("\n" + "Enter your name: ").capitalize()
        ListOfNames.append(Name)
        print("Successfully added!" + "\n")
    elif Menu == "2":
        print("\n" + "List of names:")
        print(ListOfNames)
        print("")
    elif Menu == "3":
        Index = int (input("Enter index: "))
        Update = input("Enter new name: ").capitalize()
        ListOfNames[Index] = Update
        print("Successfully updated!" + "\n")
    elif Menu == "4":
        Name = input("Enter name to delete: ").capitalize()
        ListOfNames.remove(Name)
        print("Successfully deleted!" + "\n")
    elif Menu == "5":
        print("Process ended.")
        print("Thank you, come again.")
        break
    elif Menu == "":
        print("\n" + "No input, please try again." + "\n")
        Menu = True
    else:
        print("\n" + "Invalid input, please try again." + "\n")
