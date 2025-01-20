import yaml
import os

#  Load the environment variables from the .env file
import re

from dotenv.main import load_dotenv
from pathlib import Path
import json

# load_dotenv()
# ---------- HELPER FUNCTION ----------
# Function to extract personal information from a resume
from utils import get_document_text


# def load_dotenv_with_errors():
#     # Get env file path
#     dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'data_folder', 'input', '.env')

#     load_dotenv(dotenv_path=dotenv_path)
#     # make sure env variables are set
#     if not os.getenv("CARLETON_USERNAME"):
#         raise ValueError("Please set the environment variable CARLETON_USERNAME in the .env file.")
#     if not os.getenv("CARLETON_PASSWORD"):
#         raise ValueError("Please set the environment variable CARLETON_PASSWORD in the .env file.")
#     if not os.getenv("OPENAI_API_KEY"):
#         raise ValueError("Please set the environment variable OPENAI_API_KEY in the .env file.")
#     return_object = {
#         "CARLETON_USERNAME": os.getenv("CARLETON_USERNAME"),
#         "CARLETON_PASSWORD": os.getenv("CARLETON_PASSWORD"),
#         "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
#     }
#     print("Environment variables loaded successfully.")
#     return return_object


    
# Get personal_info from resume with ai
def get_resume_path():
    
    relative_dir = Path('./data_folder/input/resume/')
    absolute_dir = (Path(__file__).parent / relative_dir).resolve()
    pdf_resume_files = list(absolute_dir.glob('*.pdf'))

    if not pdf_resume_files:
        raise FileNotFoundError("No PDF files found in the resume folder.")

    resume_path = pdf_resume_files[0]
    print(f"Successfully loaded resume from: {resume_path}")
    return resume_path

def get_personal_info_from_resume():
    # Get personal_info from resume with ai
    resume_path = get_resume_path()
    resume_text = get_document_text(str(resume_path))
    # personal_info = extract_personal_information_from_resume(resume_text)
    print(f"Successfully extracted personal information from resume: {resume_path}")
    return resume_text
    
def make_regex_from_keywords(keywords):
    if not keywords:  # If keywords list is empty
        return ".*"  # Match anything
    # Join the keywords with | and make the pattern case-insensitive
    pattern = "(?i)(" + "|".join(map(re.escape, keywords)) + ")"
    return pattern

def get_regex_from_keywords():
    # Get keywords from the user
    user_info = load_config()  # Assumes `load_config` is implemented
    keywords = user_info['keywords']
    # Get the regex pattern from the keywords
    regex = make_regex_from_keywords(keywords)
    # add regex to personal_info.yaml
    return regex

# Example usage
# regex_from_keywords = get_regex_from_keywords()
# print(regex_from_keywords)

# Function to load the personal information configuration from the YAML file
def load_config():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    

    # Construct the absolute path to config.yaml
    # config_path = os.path.join(script_dir, '..', 'data_folder', 'input', 'personal_info.yaml')
    config_path = "./data_folder/input/personal_info.yaml"
    # Check if the config file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at: {config_path}")
    
    # Load the YAML configuration
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    # Validate configuration
    validate_config(config)
    
    return config

def validate_config(config):
    # Required fields validation
    required_fields = {
        'name': str,
        'surname': str,
        'email': str,
        'phone': str,
        'linkedin': str,
        'github': str
    }
    # Optional fields validation
    optional_fields = {
        'keywords': list,
    }
    
    # Check required fields
    for field, expected_type in required_fields.items():
        if field not in config:
            raise ValueError(f"Missing required field '{field}' in config file")
        if not isinstance(config[field], expected_type):
            raise TypeError(f"Field '{field}' must be of type {expected_type}")

    # Check optional fields
    for field, expected_type in optional_fields.items():
        if field in config and not isinstance(config[field], expected_type):
            print(f"Warning: Optional field '{field}' should be of type {expected_type}")


def update_config_with_personal_info(config):
    if not config:
        raise ValueError("Config is empty")

    personal_info = get_personal_info_from_resume()
    regex = get_regex_from_keywords()
    
    config['regex'] = regex
    config['personal_information'] = personal_info

    return config



# funciton to load secrets
def load_secrets():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path to secrets.json
    secrets_path = os.path.join(script_dir, './data_folder/input/secrets.yaml')
    # Check if the secrets file exists
    if not os.path.exists(secrets_path):
        raise FileNotFoundError(f"Secrets file not found at: {secrets_path}")
    # Load the secrets YAML file
    with open(secrets_path, 'r') as file:
        secrets = yaml.safe_load(file)

    #set the environment variables
    os.environ["CARLETON_USERNAME"] = secrets["CARLETON_USERNAME"]
    os.environ["CARLETON_PASSWORD"] = secrets["CARLETON_PASSWORD"]

    # use either google api key or openai api key
    if "GOOGLE_API_KEY" in secrets:
        os.environ["GOOGLE_API_KEY"] = secrets["GOOGLE_API_KEY"]
        print("Google API Key set")
    elif "OPENAI_API_KEY" in secrets:
        os.environ["OPENAI_API_KEY"] = secrets["OPENAI_API_KEY"]
        print("OpenAI API Key set")
    

    return secrets

# print(load_secrets())
# config = load_config()
# print(config)