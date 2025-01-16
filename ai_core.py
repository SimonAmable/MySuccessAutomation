# # This file has the main ai cover letter customization core logic for the project...



# # This File includes
# # -  the logic for extracting job information from job descriptions
# # -  the logic for generating cover letters

# # Import the necessary modules
# from langchain_core.output_parsers import JsonOutputParser
# from langchain_core.prompts import PromptTemplate
# from pydantic import BaseModel, Field
# from langchain_openai import ChatOpenAI
# from langchain_community.document_loaders import PyPDFLoader


# # --------- Initialize the LLM model ---------
# # TODO: ALlow the user to choose the model (good because google is free)
# import getpass
# import os

# if not os.environ.get("OPENAI_API_KEY"):
#   os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# from langchain_openai import ChatOpenAI
# import glob
# from loggin import print
# model = ChatOpenAI(model="gpt-4o-mini")

# ###---------------- Extracting relevant job information from job description ------------------
# # Define the data structure for the job information using Pydantic
# class JobInformation(BaseModel):
#     title: str = Field(description="The job title")
#     company: str = Field(description="The company offering the job")
#     location: str = Field(description="The job location")
#     responsibilities: list = Field(description="A list of job responsibilities")
#     qualifications: list = Field(description="A list of job qualifications")
#     benefits: list = Field(description="A list of job benefits")
#     skills: list = Field(description="A list of required technical skills for the job, such as SQL, Python, etc.")

# def extract_job_information(job_description: str) -> JobInformation:
#     """
#     Extracts structured job information from a job description string.
#     Parameters:
#         job_description (str): The job description text to extract information from.
#     Returns:
#         JobInformation: A data structure containing the extracted job details.
#     """

#     # Initialize the JSON output parser with the defined data structure
#     job_info_parser = JsonOutputParser(pydantic_object=JobInformation)
    
#     # Define the prompt template for extracting job information
#     job_info_prompt = PromptTemplate(
#         template="Answer the user query.\n{format_instructions}\n{query}\n",
#         input_variables=["Extract all relevant job information from the job description."],
#         partial_variables={"format_instructions": job_info_parser.get_format_instructions()},
#     )
    
#     # Create a chain of the prompt and model, then parse the response
#     chain = job_info_prompt | model | job_info_parser
    
#     # Invoke the chain with the job description to extract job information
#     return chain.invoke({"query": job_description})



# def get_all_pdf_text(pdf_path: str) -> str:
#     """
#     Extracts text from all pages of a PDF file.
    
#     Parameters:
#         pdf_path (str): Path to the PDF file
        
#     Returns:
#         str: Combined text from all pages of the PDF
#     """
#     loader = PyPDFLoader(pdf_path)
#     pages = loader.load()
#     return ' '.join(page.page_content for page in pages)




# ### --------------- Extracting personal information from resume 

# # Define your desired data structure.
# class PersonalInformation(BaseModel):
#     name: str = Field(description="The person's first name")
#     surname: str = Field(description="The person's last name")
#     email: str = Field(description="The person's email address")
#     phone: str = Field(description="The person's phone number")
#     linkedin: str = Field(description="The person's LinkedIn profile URL")
#     github: str = Field(description="The person's GitHub profile URL")
#     portfolio: str = Field(description="The person's personal portfolio URL")
#     address: str = Field(description="The person's address")
#     summary: str = Field(description="A brief summary about the person")
#     experience: list = Field(description="A list of the person's work experiences")
#     skills: list = Field(description="A list of the person's skills")
#     education: list = Field(description="A list of the person's educational background")

# # Get sample resume text
# with open('../data_folder/input/plain_resume.txt', 'r') as file:
#     sample_resume = file.read()

# # Function to extract personal information from a resume
# def extract_personal_information_from_resume(resume_text):

#     # Initialize the JSON output parser with the defined data structure
#     personal_information_parser = JsonOutputParser(pydantic_object=PersonalInformation)
#     # Define the prompt template for extracting personal information from a resume
#     personal_info_extraction_prompt = PromptTemplate(
#         template="Answer the user query.\n{format_instructions}\n{query}\n",
#         input_variables=["Extract all relevant personal information from the resume."],
#         partial_variables={"format_instructions": personal_information_parser.get_format_instructions()},
#     )

#     # Define the chain of operations for extracting personal information
#     chain = personal_info_extraction_prompt | model | personal_information_parser

#     # Invoke the chain with the resume text
#     result = chain.invoke({"query": resume_text})

#     # Return the extracted personal information
#     return result.output

# # Extract and save personal information to a variable & file for later use
# # Set up logging
# # logging.basicConfig(level=logging.INFO)

# # Look for PDF files in the resume folder
# resume_pdf_files = glob.glob('../data_folder/input/resume/*.pdf')

# if resume_pdf_files:
#     # Use the first PDF file found
#     resume_text = get_all_pdf_text(resume_pdf_files[0])
#     personal_info = extract_personal_information_from_resume(resume_text)
#     print(f"Extracted information from PDF: {resume_pdf_files[0]}")
# else:
#     # Fallback to the plain text resume if no PDF is found
#     print("No PDF files found in resume folder. Please put a .pdf resume file into the 'resume' folder.")
#     personal_info = extract_personal_information_from_resume(sample_resume)


# # Create the cover letter from the extracted personal information and job information




