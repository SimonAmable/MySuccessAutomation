import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys

# Color scheme
BG_COLOR = "#1a1a1a"  # Dark background
TEXT_COLOR = "#ffffff"  # White text
BUTTON_BG = "#2d2d2d"  # Dark button background
BUTTON_FG = "#00ff00"  # Green text for buttons
HOVER_COLOR = "#3d3d3d"  # Lighter color for button hover

def button_hover_enter(button):
    button.configure(background=HOVER_COLOR)

def button_hover_leave(button):
    button.configure(background=BUTTON_BG)

# Function to run scripts
def run_script(script_name):
    try:
        # Get absolute path to script
        script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), script_name)
        
        if os.name == 'nt':  # Windows
            # Use cmd /k to keep window open
            cmd = ['cmd', '/k', sys.executable, script_path]
            subprocess.Popen(cmd, 
                           creationflags=subprocess.CREATE_NEW_CONSOLE,
                           shell=False)
        else:  # Unix
            subprocess.Popen(['xterm', '-e', sys.executable, script_path])
            
        print(f"Launched {script_name} in new window")
    except Exception as e:
        print(f"Error launching script: {e}")
        # Optional: show error in GUI
        messagebox.showerror("Error", f"Failed to run {script_name}: {str(e)}")
# Function to clear the Tkinter window
def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

# Main menu
def main_menu(window):
    clear_window(window)
    window.title("AI Job Application Automation")
    window.configure(bg=BG_COLOR)

    tk.Label(window, text="Welcome to AI-COC!", font=("Helvetica", 16, "bold"),
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    tk.Label(window, text="Please select an option:", font=("Helvetica", 12),
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)

    buttons = [
        ("1. Start the program", lambda: start_option_menu(window)),
        ("2. View the README file", view_readme),
        ("3. Exit the program", exit_program)
    ]

    for text, command in buttons:
        btn = tk.Button(window, text=text, command=command, width=30,
                       bg=BUTTON_BG, fg=BUTTON_FG, relief="flat")
        btn.bind("<Enter>", lambda e, b=btn: button_hover_enter(b))
        btn.bind("<Leave>", lambda e, b=btn: button_hover_leave(b))
        btn.pack(pady=5)

# Start the program menu
def start_option_menu(window):
    clear_window(window)
    window.configure(bg=BG_COLOR)
    # window.title("AI Job Application Automation")
    tk.Label(window, text="Starting the program...", font=("Helvetica", 12),
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    tk.Label(window, text="Please select an option:", font=("Helvetica", 12),
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)

    buttons = [
        ("1. Automatically Apply to Jobs", lambda: auto_apply(window)),
        ("2. Automatically Create Cover Letters", lambda: auto_create_cover_letter(window)),
        ("3. Back to Main Menu", lambda: main_menu(window))
    ]

    for text, command in buttons:
        btn = tk.Button(window, text=text, command=command, width=30,
                       bg=BUTTON_BG, fg=BUTTON_FG, relief="flat")
        btn.bind("<Enter>", lambda e, b=btn: button_hover_enter(b))
        btn.bind("<Leave>", lambda e, b=btn: button_hover_leave(b))
        btn.pack(pady=5)

# View the README file
def view_readme():
    if os.name == 'nt':  # Windows
        os.system("notepad README.md")
    else:  # macOS/Linux
        subprocess.run(["xdg-open", "quick_start_readME.md"])

# Exit the program
def exit_program():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        sys.exit()

# Automatically apply to jobs
def auto_apply(window):
    clear_window(window)
    window.configure(bg=BG_COLOR)
    
    tk.Label(window, text="Starting the automatic job application process...", 
             font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    run_script("auto_apply.py")
    tk.Label(window, text="Job application process complete!", 
             font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    btn = tk.Button(window, text="Back to Menu", command=lambda: start_option_menu(window),
                    width=30, bg=BUTTON_BG, fg=BUTTON_FG, relief="flat")
    btn.bind("<Enter>", lambda e, b=btn: button_hover_enter(b))
    btn.bind("<Leave>", lambda e, b=btn: button_hover_leave(b))
    btn.pack(pady=10)

# Automatically create cover letters
def auto_create_cover_letter(window):
    clear_window(window)
    window.configure(bg=BG_COLOR)
    
    tk.Label(window, text="Starting the automatic cover letter creation process...", 
             font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    run_script("auto_create_cover_letters.py")
    tk.Label(window, text="Cover letter creation process complete!", 
             font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)
    btn = tk.Button(window, text="Back to Menu", command=lambda: start_option_menu(window),
                    width=30, bg=BUTTON_BG, fg=BUTTON_FG, relief="flat")
    btn.bind("<Enter>", lambda e, b=btn: button_hover_enter(b))
    btn.bind("<Leave>", lambda e, b=btn: button_hover_leave(b))
    btn.pack(pady=10)

# Initialize Tkinter window
def main():
    window = tk.Tk()
    window.geometry("400x300")
    window.configure(bg=BG_COLOR)
    main_menu(window)
    window.mainloop()

if __name__ == "__main__":
    main()
