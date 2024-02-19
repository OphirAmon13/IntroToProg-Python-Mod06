# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: Ophir Amon, 2/19/2024
# ------------------------------------------------------------------------------------------ #

# Import necessary functions
from sys import exit
import json
from json.decoder import JSONDecodeError

# Define the Data Variables and constants
MENU: str = '''
    ---- Course Registration Program ----
    Select from the following menu:  
        1. Register a Student for a Course.
        2. Show current data.  
        3. Save data to a file.
        4. Exit the program.
    ----------------------------------------- 
    '''
FILE_NAME: str = "Enrollments.json"
menu_choice: str = "" # Hold the choice made by the user.
students: list = []  # A table of student data

# Define the classes to organize code
class FileProcessor: # Stores all functions that have to do with .json files
    
    # Function to output error message whereever needed
    @staticmethod
    def output_error_message(message: str, error: Exception = None): 
        print(message)
        print(f"Error detail: {error}")

    # Function that reads and prints the data from a file
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            with open(file_name, "r") as file:
                loaded_student_table = json.load(file)
                for item in loaded_student_table:
                        student_data.append(item)
                print(student_data)
        except FileNotFoundError as error_message:
            FileProcessor.output_error_message(f"There was an error finding the {file_name} file!", error_message)
        except JSONDecodeError as error_message:
            FileProcessor.output_error_message(f"There was an error reading the data from the {file_name} file!", error_message)
        except Exception as error_message:
            FileProcessor.output_error_message(f"There was an error reading the data from the {file_name} file!", error_message)
    
    # Function that saves data to a file
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list): # Saves all information to JSON file
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
                print(student_data)
                for row in student_data:
                    print(f"You have registered {row["first_name"]} {row["last_name"]} for {row["course_name"]}.")
        except Exception as error_message:
            FileProcessor.output_error_message(f"There was an error saving the data to the {file_name} file!", error_message)
        
class IO:

    # Function that prints the menu options
    @staticmethod
    def output_menu(menu: str): # Prints the menu of options
        print(menu)

    # Function that stores the user's menu choice 
    @staticmethod
    def input_menu_choice(): # 
        return input("Please enter a menu option (1-4): ")

    # Function that allows user to add students to the data
    @staticmethod
    def input_student_data(student_data: list): # Adds user to database
        student_first_name = input("Enter the student's first name: ")
        if not student_first_name: # Checks if student_first_name is an empty string
            print("ERROR: Student first name cannot be empty!")
            return
        
        student_last_name = input("Enter the student's last name: ")
        if not student_last_name: # Checks if student_last_name is an empty string
            print("ERROR: Student last name cannot be empty!")
            return
        
        course_name = input("Please enter the name of the course: ")
        if not course_name: # Checks if course_name is an empty string
            print("ERROR: Course name cannot be empty!")
            return
        
        student_data_dict = {   # Creates dictionary of the inputted student data
            "first_name": student_first_name,
            "last_name": student_last_name,
            "course_name": course_name,
        }
        student_data.append(student_data_dict) # Adds dictionary to list of all student data
        print(student_data)

    # Function that prints out the current data
    @staticmethod
    def output_student_courses(student_data: list): # Presents all information to the user
        print("First Name \tLast Name \tCourse Name")
        for row in student_data:
            print(f"{row["first_name"]} \t\t{row["last_name"]} \t\t{row["course_name"]}")

    # Function that ends the program
    @staticmethod
    def quit_program(): # Ends the program
        exit()

if __name__ == "__main__":

    FileProcessor.read_data_from_file(FILE_NAME, students)

    while True:
        # Present the menu of choices
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()
           
        # Checks the user's menu choice against different cases           
        match menu_choice:
            case "1":
                IO.input_student_data(students)
            case "2":
                IO.output_student_courses(students)     
            case "3":
                FileProcessor.write_data_to_file(FILE_NAME, students)
            case "4":
                IO.quit_program()
            case _:
                print("ERROR: Please select a valid option")