Employee = []

class EmployeeInfo:

    def __init__(data, name, department, position, rate):
        data.name = name
        data.department = department
        data.position = position
        data.rate = rate

while True:
    print("==========================" + "\n"
          "EMPLOYEE MANAGEMENT SYSTEM" + "\n" +
          "1 - Add employee" + "\n" +
          "2 - Hourly of employee" + "\n" +
          "3 - Display employee info" + "\n" +
          "4 - Exit/Stop" + "\n" +
          "==========================" + "\n")
    Menu = input("Choose one from the menu: ")
    if Menu == "1":
        name = input("\n" + "Enter employee name: ").title()
        department = input("Enter department: ").upper()
        position = input("Enter position: ").capitalize()
        rate = int(input("Enter rate: "))
        Employee.append(EmployeeInfo(name, department, position, rate))
        print("Successfully added!" + "\n")
    elif Menu == "2":
        index = int(input("\n" + "Enter index of employee: "))
        print(Employee[index].name, "is selected.")
        hour = int(input("Enter hourly of employee: "))
        print(Employee[index].rate * hour, "\n") 
    elif Menu == "3":
        for info in Employee:
            print("\n" + "Employee information:" +
                  "\n" + "Name:", info.name +
                  "\n" + "Department:", info.department +
                  "\n" + "Position:", info.position +
                  "\n" + "Rate:", info.rate, "\n")
    elif Menu == "4":
        print("\n" + "Program terminated.")
        break
    elif Menu == "":
        print("\n" + "No input, please try again." + "\n")
    else:
        print("\n" + "Invalid input, please try again." + "\n")
