# MySuccessAutomation: Your AI-Powered Coop Assistant 🚀

## Your Co-op Advantage. Get more interviews by automating your MySuccess applications with AI.
**MAKE VIDEO AND PUT VIDEO LINK SIMON**

Please read this readME.md for instructions and message me if you need any help, granted the readME.md is thorough so read it twice please it should only take a few minutes to complete everything. video tutorial comming very soon. ALSO this project is completely free and took a lot of time tbh so give this github project a 🌟 while your at the top of the page or if you found it useful in the end! ;) 

## Supercharge Your Carleton Co-op Job Search: Introducing MySuccessAutomation 🌟

Are you a Carleton University student tired of spending countless hours searching for co-op jobs on MySuccess and manually filling out the same applications over and over again? **MySuccessAutomation** is your ultimate co-op job search companion, built specifically for **Carleton University's MySuccess portal**! This innovative tool combines the power of **artificial intelligence** and **intelligent web automation** to find ideal job matches, craft personalized cover letters, and even **submit applications** on your behalf! Get ready to land more interviews and unlock your dream co-op placement faster than ever before!


---

## Key Features Tailored for Carleton's MySuccess 🛠️

*   **Intelligent Job Matching on MySuccess:** MySuccessAutomation uses advanced algorithms to analyze your skills, experience, and preferences, matching you with the most relevant co-op job postings on **Carleton's MySuccess platform** based on **specific keywords** you define.
*   **AI-Driven Cover Letter Generation:** Leveraging cutting-edge AI models like **OpenAI and Gemini**, the tool automatically generates compelling and tailored cover letters that showcase your unique qualifications and resonate with each specific job description found on MySuccess.
*   **Automated Application Submission on MySuccess:** Say goodbye to manual form-filling! MySuccessAutomation intelligently navigates **Carleton's MySuccess portal** and **automatically submits your applications**, saving you valuable time and effort.
*   **Effortless Configuration:** Easily customize your search criteria, personal details, and application preferences through intuitive YAML configuration files.
*   **Seamless Resume Integration:** The system extracts key information from your resume to personalize each cover letter and application, ensuring consistency and accuracy.
*   **User-Friendly Experience:** With a simple setup and intuitive interface, you can start automating your co-op job search within minutes.

---

## What You Need to Do: Quick Setup Guide ⚡

Ready to take your co-op job search to the next level? Here's how to get started:

1. **Prepare the Documents:**
    *   **Crucially**, have your latest **resume** and **transcript** already uploaded to MySuccess. The script currently only tailors your cover letter for each application and uses your most recently uploaded resume and transcript from MySuccess.
2. **Organize Your Files:**
    *   **All important information you must provide is in the folder "./data_folder/input/"**.
    *   Place your PDF resume in the `/resume` folder. MySuccessAutomation will intelligently extract personal information about you, like skills, experience, education, and more, to personalize your applications.
3. **Configure Your Preferences:** `personal_information.yaml`
The `personal_information.yaml` file is where you provide your personal details and customize your job search preferences. This file is crucial for tailoring your applications and cover letters. Here's a breakdown of each field:

*   **`keywords`**:
    *   This section defines the keywords that MySuccessAutomation will use to filter job postings on Carleton's MySuccess portal.
    *   Add keywords that match your desired job titles, skills, or industries.
    *   Be as specific or general as you like. For example, you can use "Software Engineer," "Data Science," "Machine Learning," "AWS," or "Web Development."
    *   Add each keyword on a new line, indented with two spaces, and preceded by a hyphen (`-`).
*   **`name`**:
    *   Enter your first name here.
*   **`surname`**:
    *   Enter your last name here.
*   **`email`**:
    *   Enter your email address. This will be used in your cover letters and applications.
*   **`phone`**:
    *   Enter your phone number. This will be used in your cover letters and applications.
*   **`linkedin`**:
    *   Enter the full URL of your LinkedIn profile. This will be used in your cover letters and applications.
*   **`github`**:
    *   Enter the full URL of your GitHub profile. This will be used in your cover letters and applications.
*   **`portfolio`**:
    *   Enter the full URL of your personal portfolio website. This will be used in your cover letters and applications.

**Important Notes:**

*   Do not delete any fields (keys) in the `./data_folder/input/personal_information.yaml` file, even if you don't want to use them.
*   If you don't want to include a particular field, leave its value blank (e.g., `portfolio: ""`).
*   Ensure that the file is correctly formatted according to YAML syntax. You can use online YAML validators to check for errors.
*   **Example:**

    ```yaml
    keywords:
      - "Python"
      - "Software Development"
      - "Machine Learning"
      - "AWS"

    name: "YourName"
    surname: "YourSurname"
    email: "your.email@example.com"
    phone: "123-456-7890"
    linkedin: "https://www.linkedin.com/in/yourprofile/"
    github: "https://github.com/yourusername"
    portfolio: ""
    ```
### 4. Providing Your Credentials Securely: `secrets.yaml`

The `secrets.yaml` file is where you store sensitive credentials required for MySuccessAutomation to operate. **Your security is a top priority.** This information is stored locally on your machine and is never transmitted externally.

**Important:** This file is named `secrets.yaml` and is located in the `./data_folder/input/` directory.

Here's a breakdown of the required fields:

*   **`CARLETON_USERNAME`**:
    *   Enter your Carleton University MySuccess username as a string.
    *   **Example:**  `CARLETON_USERNAME: "your_username"`
*   **`CARLETON_PASSWORD`**:
    *   Enter your Carleton University MySuccess password as a string.
    *   **Example:** `CARLETON_PASSWORD: "your_password"`
*   **`GOOGLE_API_KEY`**:
    *   Enter your Google API key as a string. This is used for accessing Google's AI services (Gemini). (this is pretty much just OPENAI's chatgpt but its COMPLETELY FREE for a api key as oposed to open ai. If you have a OPENAI api key or prefer to wish that please leave GOOGLE_API_KEY blank and uncomment/fill the OPENAI_API_KEY in the super_duper_secrets.yaml file)
    *   You can obtain a free API key by signing up here: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
    *   **Example:** `GOOGLE_API_KEY: "your_api_key"`

**Security Considerations:**

*   **Local Storage:** All data in `super_duper_secrets.yaml` is processed and stored **exclusively on your local machine**.
*   **No External Transmission:** Your credentials are **never sent to any external servers or services.**
*   **.gitignore:** The `super_duper_secrets.yaml` file is included in the project's `.gitignore` file. This prevents it from being accidentally committed to your Git repository, ensuring your credentials remain private.
*   **Responsibility** While this project takes measures to protect your data locally, always be cautious when handling sensitive information.

**Example `super_duper_secrets.yaml`:**

```yaml
CARLETON_USERNAME: "BugsBunny"  # Replace with your Carleton username
CARLETON_PASSWORD: "MySuperSecurePassword"  # Replace with your Carleton password
GOOGLE_API_KEY: "AIzaSyDOC-your_key_here-V2vB"  # Replace with your Google API key


> **Personal Note from the Developer:**
Apologies for the delayed release. Juggling a major project i've yet to release, school, and work commitments has been quite the challenge. I haven't personally used MySuccessAutomation in 2024, but only because I'm not in the co-op program this year for unrelated reasons. For any employeers or people willing to refer me : I'm open to work opportunities for the summer of 2025 though! #SomeonePleaseGiveMeAJob

---


## Installation and Execution: Step-by-Step Instructions 🌐

Follow these simple steps to get MySuccessAutomation up and running:

**1. Clone the Repository:**

```bash
git clone https://github.com/yourusername/MySuccessAutomation.git
cd MySuccessAutomation # make sure your terminal is open in the corrent folder)
```

**2. Set Up a Virtual Environment (Recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate      # On Windows
```

**3. Install Required Packages:**

```bash
pip install -r requirements.txt
```

**4. Run MySuccessAutomation:**

```bash
python auto_apply.py
```

---


## Troubleshooting: Your Quick Fix Guide 🛠️

*   **Resume Not Found?**
    *   Make sure your resume is a PDF and placed in the `/resume` folder.
*   **YAML Errors?**
    *   Verify that your `personal_information.yaml` file is correctly formatted. Online YAML validators can be helpful. Don't delete keys, but leave values blank if unwanted or not used.
*   **Dependency Installation Issues?**
    *   Ensure you're using a compatible Python version (Python 3.8+ is recommended) and have an updated `pip`: `pip install --upgrade pip`.
*   **Application Submission Errors:**
    *   **Important:** This tool is designed **specifically for Carleton University's MySuccess co-op portal**. Ensure you are using it only for applications on that platform.

---

## The Future is Bright: Our Development Roadmap 🛤️

I'm dedicated to continuously enhancing MySuccessAutomation (granted i'm working on a different project currently). Here's what's on the horizon:

*   **Broader Format Support:** Add compatibility for other file formats, such as `.docx`.
*   **Resume Customization:** Automatically tailor your resume to align with each job description's specific requirements on MySuccess.
*   **Enhanced AI:** Improve AI models usage for custom job matching, better cover letter generation, and application submission capabilities within the MySuccess platform.
*   
---

## I'm Here to Help: Support and Assistance 🤝

Need help with anything or have questions? I'm here for you! Please email me of contact one of my social medias for the fastest reply

*   **Email:** Simonamable@gmail.com
*   **GitHub Issues:** [Submit an issue](https://github.com/Simonamable/MySuccessAutomation/issues)

---

## Frequently Asked Questions: Your Answers Await ❓

*   **Q: Is MySuccessAutomation compatible with Mac, Windows, and Linux?**
    *   **A:** Yes! It's designed for cross-platform compatibility. Just make sure Python and the required dependencies are installed. (only tested on windows currently i'll admit)
*   **Q: How secure is my data?**
    *   **A:** Your data security is my top priority. All data processing occurs locally on your machine. No sensitive information is transmitted to external servers.
*   **Q: Will this work for jobs outside of Carleton's MySuccess?**
    *   **A:** No, **MySuccessAutomation is specifically designed for Carleton University's MySuccess co-op portal.** It will not function correctly with other job boards or application systems.

---

## Join the Movement: Contribute to MySuccessAutomation 🛠️

We believe in the power of community! Your contributions can help make MySuccessAutomation even better.

Here's how you can contribute:

1. **Fork** the repository.
2. **Create a new branch** for your feature or bug fix.
3. **Submit a pull request** with a clear description of your changes.

If you dont wanna do anything technical and want some help dont hesitate to send me a email at [simonamable@gmail.com](mailto:simonamable@gmail.com), or message me on discord @ : simon3421

---

## Giving Credit Where It's Due: Credits and Acknowledgements 📚

*   **Inspiration:** The architectural redesign of MySuccessAutomation was inspired by the innovative [AI Hawk](https://github.com/feder-cr/Jobs_Applier_AI_Agent)  (I read their README but havent used it yet because i got no time lolololololololololololol).
*   **A Heartfelt Thank You:** Big thanks to Adilet and all our amazing testers for their invaluable feedback and contributions.

---

## License 🔒

MySuccessAutomation is released under the MIT License. See the `LICENSE` file for more details. This project was made for educational purposes. The creator is not liable for anything.
