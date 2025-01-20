import os

import re

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from configs import load_config, update_config_with_personal_info, get_personal_info_from_resume, get_regex_from_keywords,load_secrets
from tailor_cover_letter import make_and_save_cv_from_job_desc
# Load login credentials from .env file. Ensure python-dotenv is installed.
from dotenv import find_dotenv, load_dotenv
from loggin import print
# Initialize and update configurations with personal information
configs = load_config()
configs = update_config_with_personal_info(configs)



# print("Configurations loaded successfully:")
# print(configs)

from utils import JobToID
import json

def initialize_driver():
    """Set up and return the Chrome WebDriver with specified window size."""
    print("Initializing WebDriver")
    driver = webdriver.Chrome()
    driver.set_window_size(784, 816)
    driver.implicitly_wait(10)  # Removed implicit wait
    return driver

def login(driver, username, password):
    """Automate the login process to the student portal."""
    print("Starting login process")
    driver.get("https://mysuccess.carleton.ca/notLoggedIn.htm")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a:nth-child(4) strong"))).click()
    
    print(f"Page title after clicking login: {driver.title}")
    
    userNameInput = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID, "userNameInput"))
    userNameInput.send_keys(username)
    
    driver.find_element(By.ID, "passwordInput").send_keys(password)
    driver.find_element(By.ID, "submitButton").click()
    
    try:
        print("Attempting to click the student portal link.")
        student_portal_link = WebDriverWait(driver, 5).until(
            lambda x: x.find_element(By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(4) > span:nth-child(1) > span:nth-child(1) > strong:nth-child(1)")
        )
        student_portal_link.click()
    except TimeoutException:
        print("Extra page did not appear, proceeding with login.")
    
    print("Login successful.")

def navigate_to_coop_jobs(driver):
    """Navigate to the Co-op jobs section within the student portal."""
    print("Navigating to Co-op jobs page.")
    driver.get("https://mysuccess.carleton.ca/myAccount/co-op/coopjobs.htm")
    JobPageSelectionChoosen = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.LINK_TEXT, "For My Program"))
    JobPageSelectionChoosen.click()
    print("Reached Co-op jobs page.")

def navigate_to_job_page_number(driver, page_number):
    """Navigate to a specific job page by its page number."""
    print(f"Navigating to job page number: {page_number}")
    link_text = str(page_number)
    jobPageLink = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, f"//a[@href='javascript:void(0)' and contains(text(), '{link_text}')]"))
    # Scroll to the job page link before clicking
    actions = ActionChains(driver)
    actions.move_to_element(jobPageLink).perform()
    # Click the job page link
    jobPageLink.click()
    print(f"Navigated to job page number: {page_number}")

def open_job_links(driver):
    """Retrieve all job links available on the current page."""
    print("Retrieving job links.")
    WebDriverWait(driver, 10).until(lambda x: x.find_elements(By.XPATH, "//table[@id='postingsTable']//a[contains(@class, 'np-view-btn')]"))
    link_elements = driver.find_elements(By.XPATH, "//table[@id='postingsTable']//a[contains(@class, 'np-view-btn')]")
    print(f"Found {len(link_elements)} job links.")
    return link_elements

def close_job_page(driver):
    """Close the currently opened job page and switch back to the main window."""
    print("Closing job page.")
    if len(driver.window_handles) == 2:
        driver.close()
        print("Closed the job page tab.")
    else:
        print("No additional job page to close. Potential issue encountered.")
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 10).until(lambda d: d.title)
    print("Switched back to the main window.")

def create_and_send_application_package(driver, job_name):
    """Create and send an application package for the specified job."""
    print(f"Creating and sending application package for: {job_name}")
    
    WebDriverWait(driver, 10).until(lambda d: d.title)
    print(f"Current page title: {driver.title}")
    
    uploadDocBut2 = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, "//input[@value='customPkg']"))
    uploadDocBut2.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "packageName")))
    
    packageName = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID, "packageName"))
    packageName.send_keys(job_name)
    
    coverLetterSelect = Select(driver.find_element(By.ID, "requiredInPackage4"))
    coverLetterSelect.select_by_index(1)  # Select the latest cover letter option
    
    resumeSelect = Select(driver.find_element(By.ID, "requiredInPackage5"))
    resumeSelect.select_by_index(1)  # Select the latest resume option
    
    gradePagesSelect = Select(driver.find_element(By.ID, "requiredInPackage6"))
    gradePagesSelect.select_by_index(1)  # Select the latest grades page option
    
    btnSubmit = driver.find_element(By.XPATH, "//input[@value='Submit Application']")
    btnSubmit.click()
    print(f"Application package has been successfully sent for: {job_name}. Good luck!")
    
    WebDriverWait(driver, 10).until(lambda d: d.title)
    print(f"Confirmed that the application package for {job_name} was sent.")

def upload_cover_letter(driver, document_name, full_file_path):
    """Upload a cover letter document for the specified job."""
    print(f"Uploading cover letter for: {document_name}")
    createNewPackageButton = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, "//input[@value='customPkg']"))
    createNewPackageButton.click()
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, "//a[normalize-space()='Click if you need to upload a new document']")).click()
    
    doc_name_input = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID, "docName"))
    doc_name_input.send_keys(document_name)
    
    doc_type_select = Select(driver.find_element(By.ID, "docType"))
    doc_type_select.select_by_value("4")  # Select cover letter type
    
    file_upload = driver.find_element(By.ID, "fileUpload_docUpload")
    file_upload.send_keys(full_file_path)

    #sleep to allow the file to upload
    time.sleep(5)
    print("waiting for the file to upload")

    # Click the submit button to upload the cover letter
    WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID, "submitFileUploadFormBtn")).click()
    print(f"Successfully uploaded cover letter for: {document_name}")
    print(f"Cover letter file path: {full_file_path}")
    
    WebDriverWait(driver, 10).until(lambda d: d.title)
    print(f"Cover letter for {document_name} has been uploaded.")

def handle_nokia_page(driver):
    """Handle any interactions specific to the Nokia page."""
    print("Handling Nokia page.")
    # TODO: Implement Nokia page handling logic
    driver.find_element()
    print("Nokia page has been handled and closed.")

def process_job_page(driver, link_element):
    """Process an individual job page by applying if it matches criteria."""
    print("Processing job page.")
    # Scroll to and open the job link in a new tab
    actions = ActionChains(driver)
    actions.move_to_element(link_element).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(link_element).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[-1])
    WebDriverWait(driver, 10).until(lambda d: d.title)
    
    urlRegex = r'https?://\S+'
    
    try:
        print("Retrieving company name...")
        company_name = WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.XPATH, "//h2[contains(@class, 'h6') and contains(@class, 'mobile--small-font') and contains(@class, 'color--font--white') and contains(@class, 'margin--t--s') and contains(@class, 'align--start')]")
        )
        
        print("Retrieving position title...")
        position_title = WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.CLASS_NAME, "np-view-question--23")
        )
        
        print("Retrieving job description...")
        job_description = WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.CLASS_NAME, "np-view-question--33")
        )
        
        print("Retrieving application method...")
        applicationMethod = WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.CSS_SELECTOR, "div[class='span8'] div:nth-child(3) div:nth-child(2)")
        )
    except TimeoutException as e:
        print(f"Failed to load element: {e.msg}")
        close_job_page(driver)
        return
    
    full_job_desc = f'{company_name.text} \n {position_title.text} \n {job_description.text} \n {applicationMethod.text}'
    expectedDocumentName = position_title.text.replace(' ', '_').replace('/', '').replace("-", "_")
    documentName = JobToID(expectedDocumentName)
    
    job_description_object = {
        "company_name": company_name.text,
        "position_title": position_title.text,
        "job_description": job_description.text,
        "application_method": applicationMethod.text
    }
    
    urlFound = re.search(urlRegex, full_job_desc, flags=re.IGNORECASE)
    if urlFound and not ("Use this system for applications" in applicationMethod.text):
        print("External job application found via URL (WE CANT APPLY TO THIS JOB). Saving description and closing page.")
        save_job_description(full_job_desc, documentName)
        close_job_page(driver)
        return
    
    try:
        print("Checking for the APPLY button.")
        button_element = WebDriverWait(driver, 1).until(lambda x: x.find_element(By.XPATH, "//body//main//div//div//div//div//div//div//button[@type='button'][normalize-space()='APPLY']"))
        if button_element:
            print("APPLY button found.")
    except TimeoutException:
        print(f"No APPLY button found for {documentName}. Possible duplicate application. Closing page.")
        close_job_page(driver)
        return
    
    regex_from_keywords = configs["regex"]
    try:
        compiled_regex = re.compile(regex_from_keywords, re.IGNORECASE)
    except re.error as e:
        print(f"Invalid regex pattern in configs['regex']: {e}")
        return
    
    print(f"Using regex pattern: {regex_from_keywords}")
    if compiled_regex.search(full_job_desc):
        print(f"Job '{documentName}' matches criteria. Initiating application process.")
        button_element.click()  # Click the APPLY button
        WebDriverWait(driver, 10).until(lambda d: d.title)
        # Check if cover letter is already created by checking file name in the list of documents
        output_folder = './data_folder/output/tailored_cover_letters/'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        # Get list of files in tailered_cover_letters
        output_folder_files = os.listdir(output_folder)
        if documentName in output_folder_files:
            print(f"Cover letter for '{documentName}' has already been automaicly created. Starting application.")
            # upload_cover_letter(driver, document_name_without_extension, cover_letter_full_file_path_pdf)
            create_and_send_application_package(driver, document_name_without_extension)
            close_job_page(driver)
            return
        #Get list of files in tailered_cover_letters
        if documentName in driver.page_source:
            print(f"Cover letter for '{documentName}' already uploaded. Skipping application.")
            close_job_page(driver)
            return
        # cover_letter_already_uploaded = False
        


        # Create and upload cover letter
        cover_letter_full_file_path = make_and_save_cv_from_job_desc(job_description_object,configs,configs['personal_information'])
        documentName = os.path.splitext(os.path.basename(cover_letter_full_file_path))[0]
        document_name_without_extension = documentName.split(".")[0]
        finished_file_directory = os.path.dirname(cover_letter_full_file_path)
        cover_letter_full_file_path_pdf = cover_letter_full_file_path.replace(".docx", ".pdf")
        print(f"Cover letter created and saved for: {documentName} at {cover_letter_full_file_path_pdf}")
        upload_cover_letter(driver, document_name_without_extension, cover_letter_full_file_path_pdf)
        create_and_send_application_package(driver, document_name_without_extension)
    else:
        print(f"Job '{documentName}' does not match criteria. Skipping application.")
        close_job_page(driver)
        return
    
    if button_element:
        print("Successfully applied for the job.")
    print(f"Processed job: {documentName}")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def save_job_description(description, file_title):
    """Save the job description to a text file within the external_appliction directory."""
    print(f"Saving job description for: {file_title}")
    folder_path = os.path.join(os.getcwd(), './data_folder/output/external_appliction')  # Directory to save descriptions
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create the directory if it doesn't exist
    
    file_name = file_title.replace(' ', '_').replace('/', '').replace("-", "_")  # Sanitize file name
    file_path = os.path.join(folder_path, f"{file_name}.txt")
    
    with open(file_path, 'w') as file:
        file.write(description)
    
    print(f"Job description saved to: {file_path}")

def save_job_description_to_json(description, file_title):
    """Save the job description to a JSON file within the external_appliction directory."""
    print(f"Saving job description for: {file_title}")
    folder_path = os.path.join(os.getcwd(), './data_folder/output/external_appliction')  # Directory to save descriptions
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create the directory if it doesn't exist
    
    file_name = file_title.replace(' ', '_').replace('/', '').replace("-", "_")  # Sanitize file name
    file_path = os.path.join(folder_path, f"{file_name}.json")
    
    with open(file_path, 'w') as file:
        json.dump(description, file, indent=4)
    
    print(f"Job description saved to: {file_path}")

def main():
    """Main function to execute the job application automation process."""
    print("Starting the job application automation script.")
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'data_folder', 'input', '.env')
    # load_dotenv(dotenv_path)
    
    # Retrieve login credentials from environment variables
    # CARLETON_USERNAME = os.getenv("MY_USERNAME")
    # CARLETON_PASSWORD = os.getenv("MY_PASSWORD")
    # Retrieve login credentials from secrets file
    secrets = load_secrets()
    CARLETON_USERNAME = secrets["CARLETON_USERNAME"]
    CARLETON_PASSWORD = secrets["CARLETON_PASSWORD"]

    configs = load_config()
    # Incorporate personal information into the configurations
    # configs["personal_info"] = get_personal_info_from_resume()
    configs = update_config_with_personal_info(configs)
    print("Updated configurations with personal information:")
    print(configs)
    print("Debugging: Configurations loaded successfully.")
    
    driver = initialize_driver()  # Initialize the WebDriver
    login(driver, CARLETON_USERNAME, CARLETON_PASSWORD)  # Log into the student portal
    navigate_to_coop_jobs(driver)  # Navigate to the Co-op jobs section
    
    # Determine the number of job pages available
    tableNum = driver.find_elements(By.TAG_NAME, "table")
    print(f"Number of tables found: {len(tableNum)}")
    numberOfPages = len(tableNum)
    
    # Iterate through each job page to process available job listings
    for page_number in range(1, numberOfPages + 1):
        link_elements = open_job_links(driver)
        
        for link_element in link_elements:
            process_job_page(driver, link_element)  # Process each individual job listing
        
        print(f"All relevant jobs from page {page_number} have been processed successfully.")
    
    print("All jobs have been searched and saved successfully.")
    driver.quit()
    print("WebDriver has been closed. Completed processing all job pages.")
    print("Job application automation script has finished execution.")

if __name__ == "__main__":
    main()
