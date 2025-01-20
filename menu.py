# Import required libraries for system operations, terminal manipulation and styling
import os
import sys
import time
import subprocess
from colorama import Fore, Style
from colorama import init

# Initialize colorama for terminal colors
init()

# Function to clear the terminal screen based on operating system
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to run Python scripts using the current interpreter
def run_script(script_name):
    python_exe = sys.executable
    subprocess.run([python_exe, script_name], shell=True)

# Main menu function - displays primary options to the user
def main_menu():
    clear()
    print(Fore.GREEN + Style.BRIGHT + "Welcome to AI-COC the Job Application Automation Program!" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Please select an option from the menu below:" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "1. Start the program" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "2. View the README file" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "3. Exit the program" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Please enter the number of the option you would like to select:" + Style.RESET_ALL)
    user_input = input()
    if user_input == "1":
        start_option_menu()
    elif user_input == "2":
        view_readme()
    elif user_input == "3":
        exit_program()
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid input, please try again" + Style.RESET_ALL)
        time.sleep(2)
        main_menu()

# Function to initiate the program and show secondary menu options
def start_option_menu():
    clear()
    print(Fore.GREEN + Style.BRIGHT + "Starting the program..." + Style.RESET_ALL)
    time.sleep(2)
    auto_apply_or_auto_create()

# Function to display README file using notepad
def view_readme():
    clear()
    print(Fore.GREEN + Style.BRIGHT + "Opening the README file..." + Style.RESET_ALL)
    time.sleep(2)
    subprocess.run(["notepad", "quick_start_readME.md"])

# Function to exit the program
def exit_program():
    clear()
    print(Fore.GREEN + Style.BRIGHT + "Exiting the program..." + Style.RESET_ALL)
    time.sleep(2)
    sys.exit()

# Function to display options for auto-apply or cover letter creation
def auto_apply_or_auto_create():
    clear()
    print(Fore.GREEN + Style.BRIGHT + "Please select an option from the menu below:" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "1. Automaticly Apply to all matching jobs" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "2. Automaticly Create Cover Letters for all jobs" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "3. Exit the program" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Please enter the number of the option you would like to select:" + Style.RESET_ALL)
    user_input = input()
    if user_input == "1":
        auto_apply()
    elif user_input == "2":
        auto_create_cover_letter()
    elif user_input == "3":
        exit_program()
    else:
        print(Fore.RED + Style.BRIGHT + "Invalid input, please try again" + Style.RESET_ALL)
        time.sleep(2)
        auto_apply_or_auto_create()

# Function to handle automatic job applications
def auto_apply():
    clear()
    print(Fore.GREEN + Style.BRIGHT + "Starting the automatic job application process..." + Style.RESET_ALL)
    time.sleep(2)
    subprocess.run(["python", "auto_apply.py"])
    print(Fore.GREEN + Style.BRIGHT + "Automatic job application process complete!" + Style.RESET_ALL)
    time.sleep(2)
    auto_apply_or_auto_create()

# Function to handle automatic cover letter creation
def auto_create_cover_letter():
    clear()
    print(Fore.GREEN + Style.BRIGHT + "Starting the automatic cover letter creation process (find cover letters in `data_folder/output/tailored_cover_letters`)." + Style.RESET_ALL)
    time.sleep(2)
    run_script("auto_create_cover_letters.py")
    print(Fore.GREEN + Style.BRIGHT + "Automatic cover letter creation process complete!" + Style.RESET_ALL)
    time.sleep(2)
    auto_apply_or_auto_create()

# Program entry point
main_menu()
