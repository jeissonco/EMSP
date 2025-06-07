# @Author: Jeisson Nino
# date: 26/05/2025

# Control version
# V1. Drafting structure of the program                                     26/05/25
# v2. Modifying the structure of the program using 
# a design pattern MVC (model view controller) advised by ChatGPT           03/06/25
# V3. Centralized version of the valid input function to cover all the inputs, rather than
#     having multiple functions just changing what it was printed

######################  Libraries  #######################
import os
import json
import re

###################  Classes  ############################

################# Functions ###############################
#This function verifies 
def validation(counter):

    user_info = ['name', 'position', 'department', 'location']
    while True:
        try:
            info = input(f"Enter employee's {user_info[counter]}: ")
            #Here I use the regular expression to check a proper user's input, just combination of letters allowed       
            if not re.match(r"^[A-Za-z\s]+$", info):
                raise ValueError(f"Invalid {user_info[counter]}, only Letters and spaces allowed.")
        #if the input is valid breaks the loop and returns the valid input
            else:
                counter+=1 
                break 
        except ValueError:
            print("Please enter a valid name ")
            
    
    return info.title(), counter

def valid_age():
    while True:
        try:
            age = int(input("Enter employee's age: "))
            if not age >= 18 and age <=70:
                raise ValueError("Invalid age, age out of valid range")
            #if the age is valid break the loop
            else:
                break 
        except ValueError:
            print("Please enter a valid age between (18-69)")

    return age


def valid_salary():

    while True:
        try:
            salary = float(input("Enter salary: "))
            #Here I use the regular expression library to check if the student name is valid

            if salary<=999:
                raise ValueError("Invalid salary, it needs to be higher than 999.")
        #if the salary meets the minimum requirements
            else:
                break 
        except ValueError:
            print("Please enter a valid position")
            
    return salary


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
    def to_dict(self): # Renamed to to_dict for standard Python naming
        return {
            "name": self.__name,
            "age": self.__age,
            "position": self.__position,
            "salary": self.__salary,
            "department": self.department,
            "location": self.location
        }

    #return a new employee instance
    def from_dict(data):
        return Employee(
            data['name'],
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

        #open the file in read mode = 'r'
        try:
            with open(self.file_path, 'r') as file:
                #loading the data into a dictionary
                data = json.load(file)

                #Converts dicts from file to Employee objects
                for emp_dict in data:
                    employee = Employee.from_dict(emp_dict)
                    employees.append(employee)
            return employees # Ensure employees list is always returned
        except (json.JSONDecodeError, FileNotFoundError) as error:
            print(f'It has been an error loading the data: {error}. Starting with an empty database.')
            return [] # Return empty list if loading fails to allow program to continue


    ######################## SAVE EMPLOYEES ##########################

    def save_employees(self, employee_list):
        try:
            #list comprehension to create and write the data as a list of dicts
            data = [employee.to_dict() for employee in employee_list]
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as error:
            print(f"Error saving data: {error}")

    ####################### ADD EMPLOYEE ################################
    def add_employee(self):
        clear_console()

        index = 0
        print("############## ADDING EMPLOYEE ##################")
        try:
            #loading the current list of employees
            employees = self.load_employees()
            
            for employee in employees:
                data = employee.to_dict()
                #validation of proper input name 
                name, index = validation(index)
                if data['name'] == name:
                    raise Exception
            
            #Age validation needs to be greater or equal than 18 and less than 70
            age = valid_age()
            
            position, index = validation(index)
            
            salary = valid_salary()
            
            department, index = validation(index)
            
            location, index =  validation(index)
    
            # Check for duplication (name and position ) to be done
            new_employee = Employee(name, age, position, salary, department, location)
            employees.append(new_employee)
            self.save_employees(employees)
            print(f"Employee '{name}' added successfully.")

        # Catch specific ValueError for int/float conversion issues
        except ValueError:
            print("Invalid input. Please enter correct data types (e.g., age as integer, salary as number).")
        # Catch if the employee name input is already in the database
        except Exception:
            print("This employee already exists in the database.")


    ############################# VIEW ALL THE EMPLOYEES ################################

    def view_all_employees(self):
        clear_console()
        print("           DATABASE             ")
        employees = self.load_employees()
        if not employees:
            print("No employee records found.")
            return

        for employee in employees:
            data = employee.to_dict()
            print(f"Name: {data['name']}, Age: {data['age']}, Position: {data['position']}, "
                  f"Salary: ${data['salary']:.2f}, Department: {data['department']}, Location: {data['location']}")


####################  functions ##########################

#Function to clear the terminal
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


####################  Main  ###############################

def main():
    database = EmployeeDatabase()

    while True:
        clear_console() # Clear console for cleaner menu display
        print("################ Employee Management System ###################")
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Update Employee Details")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Sort Employees")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            database.add_employee()
            input("Press Enter to continue...") 
        elif choice == "2":
            database.view_all_employees()
            input("Press Enter to continue...") 
        elif choice == "3":
            print("Function not yet implemented.")
            input("Press Enter to continue...")
        elif choice == "4":
            print("Function not yet implemented.")
            input("Press Enter to continue...")
        elif choice == "5":
            print("Function not yet implemented.")
            input("Press Enter to continue...")
        elif choice == "6":
            print("Function not yet implemented.")
            input("Press Enter to continue...")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 6.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()