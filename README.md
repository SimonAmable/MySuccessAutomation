# MySuccessAutomation: Your AI-Powered Coop Assistant 🚀

## How finish 100 applications in under 3 minutes:
# MAKE VIDEO AND PUT VIDEO LINK SIMON
(for now please read this readME.md for instructions and message me if you need any help, video tutorial comming very soon. Also give this github project a 🌟 <3 ;) while your at the top of the page anyways or if you found it useful in the end ;) 

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
4. **Give me your secrets** `super_duper_secrets.yaml`
    *  Fill out the `super_duper_secrets.yaml` file  in "./data_folder/input/super_duper_secrets.yaml" with all the requested details. Please refer to the video tutorial for more information! (i put a lot of work in to keep all your secrets on your machine locally and completely safe so dont worry.)
       - CARLETON_USERNAME : String
        - CARLETON_PASSWORD : String
        - GOOGLE_API_KEY : String    (Sign up for free here : https://aistudio.google.com/apikey )
       


---

## From Search to Submission on MySuccess: A Real-World Example 📄

Imagine you're a skilled computer science student at Carleton seeking a challenging software development co-op placement. Here's how MySuccessAutomation revolutionizes your job search:

1. **Keyword Definition:** You specify keywords like "Python," "Software Development," "Machine Learning," "AWS," and "Agile" in your `personal_information.yaml` file.
2. **Intelligent Matching:** MySuccessAutomation scours **Carleton's MySuccess portal**, identifying co-op postings that match your defined keywords and experience.
3. **AI-Powered Personalization:** For each matching job on MySuccess, the AI analyzes the description and your resume to craft a compelling cover letter that highlights your relevant skills and experience, such as your "extensive experience in developing Python-based applications" or your "proven expertise in deploying machine learning models on AWS using Agile methodologies."
4. **Automated Submission:** MySuccessAutomation navigates to the application page on **MySuccess**, automatically fills in the required fields using your information, attaches your resume and custom-tailored cover letter, and **submits the application** on your behalf.

This end-to-end automation frees you from the tedious application process, allowing you to focus on preparing for interviews and landing your dream co-op placement instead!

(Personal note: Sorry I'm releasing this so late. I've been working on a big project, plus school and work, and didn't put enough time into this, partially because I actually didn't use it myself in 2024, only because I'm not in co-op for unrelated reasons. \#SomeonePleaseHireMeForTheSummerOf2025)

---

## Installation and Execution: Step-by-Step Instructions 🌐

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/MySuccessAutomation.git
    cd MySuccessAutomation
    ```
2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
4. **Launch MySuccessAutomation:**

    ```bash
    python main.py
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

We're dedicated to continuously enhancing MySuccessAutomation. Here's what's on the horizon:

*   **Resume Customization:** Automatically tailor your resume to align with each job description's specific requirements on MySuccess.
*   **Enhanced AI:** Improve our AI models for even more refined job matching, cover letter generation, and application submission capabilities within the MySuccess platform.
*   **Broader Format Support:** Add compatibility for other file formats, such as `.docx`.

---

## We're Here to Help: Support and Assistance 🤝

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

*   **Inspiration:** The architectural redesign of MySuccessAutomation was inspired by the innovative [AI Hawk](https://github.com/feder-cr/Jobs_Applier_AI_Agent)  (I read their README, I gotta admit).
*   **A Heartfelt Thank You:** Big thanks to Adilet and all our amazing testers for their invaluable feedback and contributions.

---

## License 🔒

MySuccessAutomation is released under the MIT License. See the `LICENSE` file for more details. This project was made for educational purposes. The creator is not liable for anything.
