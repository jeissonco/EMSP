# @Author: Jeisson Nino
# date: 26/05/2025

# Control version
# V1. Drafting structure of the program                                     26/05/25
# v2. Modifying the structure of the program using 
# a design pattern MVC (model view controller) advised by ChatGPT           03/06/25

"""
INSTRUCTIONS

 Implement the following behaviours:  Parameterised Constructor: Initialise at least 4 employee objects with the attributes mentioned 
 above and write them into a file (.txt, .csv, or .json). Call the file Current_Employees.  Add Employee: Prompt the user to enter employee
   details and write the data to the Current_Employees file. Add validation checks to ensure no employee with the same name or position is 
   added twice.  View All Employees: Read from the Current_Employees file and display all employee records.  Update Employee Details: 
   Modify an employee's details in the Current_Employees file based on the user's input.  Delete Employee: Remove an employee's details 
   from the Current_Employees file based on the user's input.  Search Employee: Search for an employee by their name in the Current_Employees
file based on the user's input.  Sort Employees: Sort and display the employees based on salary and position in the Current_Employees file based 
on the user's input.  Implement a menu in main() that allows users to select different options, such as adding a new employee, viewing all 
employees, updating employee details, deleting an employee, searching for an employee, and sorting the employees. This should be presented to 
the user when the code runs. 
"""


######################  Libraries  #######################
import os
import json

###################  Classes  ############################

class Employee:
    def __init__(self, name, age, position, salary, department, location):
        #private attributes
        self.__name = name
        self.__age = age
        self.__position = position
        self.__salary = salary

        #public attributes
        self.department = department
        self.location = location

    #printable form of instance for the object
    def __str__(self):
        return f'{self.__name} has a position as: {self.__position}\n with {self.__age} has a salary of ${self.__salary}'
    
    #return a dictionary of all employee attributes
    def to_dicto(self):
        return {
            "name": self.__name,
            "age": self.__age,
            "position": self.__position,
            "salary": self.__salary,
            "department": self.department,
            "location": self.location
        }
    
    #return a new employee instance
    #This will belong to the class but won't required an existing obejct
    #It will take a dict and return a new instance of the class: an Employee object
    #Got this recommendation from chatGPT
    @staticmethod
    def from_dict(data):
        return Employee(
            data['aame'],
            data['age'],
            data['position'],
            data["salary"],
            data["department"],
            data['location']
        )
    
    
class EmployeeDatabase:

    #Using a relative path to ensure readability throughout different pc's 
    def __init__(self, file_path=os.path.join('Current_Employees.json')):
        self.file_path = file_path


    ############################# LOADING/READING THE JSON FILE ###################################
    def load_employees(self):
        #list to store the employee objects
        employees = []

        #checking if the file exists, if first time running the app it will return
        #an empty list becuase there are no employees yet
        if not os.path.exists(self.file_path):
            return employees

        #open the file in read mode = 'r'
        try:
            with open(self.file_path, 'r') as file:
                #loading the data into a dictionary
                data = json.load(file)

                #Converts
                for emp_dict in data:
                    employee = Employee.from_dict(emp_dict)
                    employees.append(employee) 
        except (json.JSONDecodeError, FileNotFoundError) as error:
            print(f'It has been an error loading the data: {error}')


    ######################## SAVE EMPLOYEES ##########################

    def save_employees(self, employee_list):
        try:
            #list comprehension to create and write the data as a list
            data = [employee.to_dict() for employee in employee_list]
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as error:
            print(f"Error saving data: {error}")

    ####################### ADD EMPLOYEE ################################
    def add_employee(self):

        print("############## ADDING EMPLOYEE ##################")


        try:
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            position = input("Enter position: ").strip()
            salary = float(input("Enter salary: "))
            department = input("Enter department: ").strip()
            location = input("Enter location: ").strip()

            employees = self.load_employees()

            #
            #got this recommendation from chatGPT to handle the duplicatiom
            for employee in employees:
                if employee.to_dict()["name"].lower() == name.lower() and employee.to_dict()["position"].lower() == position.lower():
                    print("Employee with same name and position already exists.")
                    return

            new_employee = Employee(name, age, position, salary, department, location)
            employees.append(new_employee)
            self.save_employees(employees)
            print("Employee added successfully.")

        #Not valid users input
        except ValueError:
            print("Invalid input. Please enter correct data types (e.g., age as integer, salary as number).")


    ############################# VIEW ALL THE EMPLOYEES ################################

    def view_all_employees(self):
        print("           DATABASE             ")
        employees = self.load_employees()

        if not employees:
            print("No employee records found.")
            return

        for employee in employees:
            data = employee.to_dict()
            # Ensure these keys match what to_dict() returns (now all lowercase)
            print(f"Name: {data['name']}, Age: {data['age']}, Position: {data['position']}, "
                  f"Salary: {data['salary']}, Department: {data['department']}, Location: {data['location']}")


        

####################  functions ##########################

#Function to clear the terminal
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


####################  Main  ############################### 

def main():

    database = EmployeeDatabase()

    while True:
        print("################ Employee Management System ###################")
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Update Employee Details")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Sort Employees")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            database.add_employee()
        elif choice == "2":
           
            database.view_all_employees()
        elif choice == "3":
            print("not yet implemented.")
            # database.update_employee() 
        elif choice == "4":
            print("not yet implemented.")
            # database.delete_employee()
        elif choice == "5":
            print("not yet implemented.")
            # database.search_employee()
        elif choice == "6":
            print("not yet implemented.")
            # database.sort_employees()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 6.")




if __name__ == "__main__":
    main()

