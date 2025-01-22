import gradio as gr
import subprocess
import sys
import yaml
import os

# Function to run a Python script
def run_script(script_name):
    python_exe = sys.executable  # Gets the current Python interpreter path
    subprocess.run([python_exe, script_name], shell=True)

# Functions corresponding to menu options
def start_program(option):
    if option == "Automatically Apply to All Matching Jobs":
        run_script("auto_apply.py")
        return "Automatic job application process complete!"
    elif option == "Automatically Create Cover Letters":
        run_script("auto_create_cover_letters.py")
        return "Automatic cover letter creation process complete!"
    else:
        return "Invalid option selected."

def view_readme():
    try:
        subprocess.run(["notepad", "README.md"])
        return "Opened README.md successfully!"
    except FileNotFoundError:
        return "README.md not found!"

def exit_program():
    return "Exiting the program... Thank you!"

# Function to save user data to a YAML file
def save_to_yaml(keywords, name, surname, email, phone, linkedin, github, portfolio, username, password, api_key, openai_key, resume):
    # Parse and clean keywords
    keywords_list = [k.strip() for k in keywords.split(",") if k.strip()]
    
    # Create the YAML structure
    user_data = {
        "keywords": keywords_list,
        "name": name,
        "surname": surname,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "portfolio": portfolio,
        "CARLETON_USERNAME": username,
        "CARLETON_PASSWORD": password,
        "GOOGLE_API_KEY": api_key,
        "OPENAI_API_KEY": openai_key if openai_key.strip() else None,
    }

    # Save the YAML file
    yaml_filename = "user_data.yaml"
    with open(yaml_filename, "w") as yaml_file:
        yaml.dump(user_data, yaml_file, default_flow_style=False)

    # Save the uploaded resume file
    if resume:
        resume_filename = os.path.basename(resume.name)
        with open(resume_filename, "wb") as resume_file:
            resume_file.write(resume.read())

    return f"YAML file '{yaml_filename}' and resume '{resume_filename}' saved successfully!"

# Define Gradio interface
def main_interface(menu_choice, sub_choice):
    if menu_choice == "Start the Program":
        return start_program(sub_choice)
    elif menu_choice == "View the README File":
        return view_readme()
    elif menu_choice == "Exit the Program":
        return exit_program()
    else:
        return "Invalid menu choice."

# Gradio components
menu_choices = ["Start the Program", "View the README File", "Exit the Program"]
sub_choices = ["Automatically Apply to All Matching Jobs", "Automatically Create Cover Letters"]

# Gradio Interface
with gr.Blocks() as gui:
    gr.Markdown("## Welcome to AI-TUAH: The Job Application Automation Program!")
    
    with gr.Tab("Main Menu"):
        gr.Markdown("### Please select an option from the menu below:")
        menu_choice = gr.Radio(menu_choices, label="Main Menu")
        sub_choice = gr.Radio(sub_choices, label="Sub Menu (for Start the Program)", visible=False)

        def toggle_sub_menu(choice):
            return gr.update(visible=(choice == "Start the Program"))

        menu_choice.change(toggle_sub_menu, menu_choice, sub_choice)

        main_output = gr.Textbox(label="Output", interactive=False)
        submit_main = gr.Button("Submit")
        submit_main.click(main_interface, inputs=[menu_choice, sub_choice], outputs=main_output)

    with gr.Tab("Input Collection"):
        gr.Markdown("### Fill in your details below to generate a YAML configuration file and upload your resume. (IM NOT FINISHED THIS RN FOLLOW GITHUB INPUT INSTRUCTIONS SORRY)")
        
        with gr.Row():
            keywords = gr.Textbox(label="Keywords (comma-separated)", placeholder="e.g., Python, AI, Automation")
            name = gr.Textbox(label="First Name", placeholder="Enter your first name")
            surname = gr.Textbox(label="Last Name", placeholder="Enter your last name")

        with gr.Row():
            email = gr.Textbox(label="Email", placeholder="Enter your email")
            phone = gr.Textbox(label="Phone", placeholder="Enter your phone number")
            linkedin = gr.Textbox(label="LinkedIn URL", placeholder="Enter your LinkedIn profile URL")

        with gr.Row():
            github = gr.Textbox(label="GitHub URL", placeholder="Enter your GitHub profile URL")
            portfolio = gr.Textbox(label="Portfolio URL", placeholder="Enter your portfolio URL")
            username = gr.Textbox(label="Carleton Username", placeholder="Enter your Carleton username")

        with gr.Row():
            password = gr.Textbox(label="Carleton Password", placeholder="Enter your Carleton password", type="password")
            api_key = gr.Textbox(label="Google API Key", placeholder="Enter your Google API key")
            openai_key = gr.Textbox(label="OpenAI API Key (optional)", placeholder="Enter your OpenAI API key (optional)")

        resume = gr.File(label="Upload Resume (PDF only)", file_types=[".pdf"])
        input_output = gr.Textbox(label="Output", interactive=False)

        submit_input = gr.Button("Generate YAML and Save Resume")
        submit_input.click(
            save_to_yaml,
            inputs=[keywords, name, surname, email, phone, linkedin, github, portfolio, username, password, api_key, openai_key, resume],
            outputs=input_output,
        )

    

# Launch the Gradio GUI
gui.launch()
