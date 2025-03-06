# Web Automated Login System

## 📚 **Project Description**
The **Automated Login System for Gunadarma University Wifi Access** is a Python-based project designed to automate the process of logging into the university's wifi network. The system uses **Selenium** to interact with the login page, input credentials, and submit the login form automatically. This project was developed to address the inefficiencies of manually logging into multiple computers in the Elementary Laboratory of Industrial Engineering at Gunadarma University.

---

## 🎯 **Goals**
1. **Automate Login Process**: Eliminate the need for manual intervention by automating the login process for the university's wifi network.
2. **Improve Efficiency**: Save time and effort for laboratory assistants by reducing the time required to log into multiple computers.
3. **Scalability**: Ensure the system can handle multiple computers simultaneously using tools like **Veyon Master**.
4. **Ease of Deployment**: Generate a standalone `.exe` file using **PyInstaller** for easy distribution and execution on any Windows system.

---

## 🛠️ **Tools and Technologies**
The project leverages the following tools and technologies:
- **Python**: The primary programming language used for scripting the automation process.
- **Selenium**: A powerful web automation library used to interact with the Gunadarma University wifi login page.
- **Visual Studio Code**: The Integrated Development Environment (IDE) used for writing, debugging, and testing the Python script.
- **Veyon Master**: Used to deploy and run the `.exe` file simultaneously on multiple computers in the laboratory.
- **PyInstaller**: A library for converting the Python script into a standalone `.exe` file.
- **ChatGPT AI**: An AI-powered coding assistant that helped debug issues, optimize code, and recommend solutions.

---

## ⚙️ **Features**
The Automated Login System includes the following key features:
- **Automated Login**: Automatically inputs credentials and submits the login form on the university's wifi portal.
- **Scalability**: Can be deployed across multiple computers using **Veyon Master**.
- **Standalone Executable**: The script is converted into a standalone `.exe` file for easy distribution and execution.
- **Error Handling**: Includes basic error handling to manage unexpected changes in the website’s structure or network issues.

---

## 🧠 **Implementation**
The core of the project is a Python script that automates the login process for the Gunadarma University wifi portal. Below are the key components of the implementation:

### **Importing Required Libraries**
The script uses **Selenium** for browser automation and **WebDriverWait** to ensure the script waits for specific elements to load before interacting with them.

### **Setting Up Credentials and Website Link**
The script targets the university's login page and uses predefined credentials for authentication.

### **Locating Web Elements**
The script identifies the HTML elements for the username, password, and submit button using their respective attributes.

### **Automating the Login Process**
The script initializes the Chrome browser, navigates to the login page, and waits for the username and password fields to load. It then inputs the credentials and clicks the submit button to complete the login process.

---

## 🚀 **How to Use**
1. **Install Dependencies**:
   Ensure you have the required Python libraries installed:
   ```bash
   pip install selenium pyinstaller
2. **Download ChromeDriver**:
   Download the appropriate version of ChromeDriver for your Chrome browser and ensure it is in your system's PATH.
3. **Run the Script**:
   Use PyInstaller to convert the script into a standalone .exe file:
   ```bash
   python automated_login.py
4. **Generate Standalone Executable**:
   Execute the Python script to automate the login process:
   ```bash
   pyinstaller --onefile automated_login.py
5. **Deploy Using Veyon Master (Optional)**:
   Use Veyon Master to deploy and run the .exe file simultaneously on multiple computers in the laboratory.

---

## 📊 **Challenges and Solutions**
While developing this application, several challenges were encountered and resolved:
- Lack of Customizability: The script is tailored specifically for the Gunadarma University login page. It may not work on other websites with different element names or structures.
- No Captcha Handling: The script cannot handle websites that use captcha for security.
- Speed: The script takes several seconds to a minute to execute, which may be slow for some users.
- Hardcoded Credentials: The script contains hardcoded credentials, making it necessary to update the code if the username or password changes.
- Dependency on Website Structure: If the website’s structure changes (e.g., element names or IDs), the script will need to be updated.
- Dependency on Veyon: The script relies on Veyon Master to run simultaneously on multiple computers, which adds an extra layer of complexity.

---

## 📝 **Recommendations for Improvement**
While the application is functional, there are areas where it can be improved:
- Dynamic Credential Input: Modify the script to accept credentials as user input or from an external file, making it more flexible and secure.
- Captcha Handling: Integrate a captcha-solving mechanism or use an alternative approach for websites with captcha.
- Error Handling: Enhance error handling to manage unexpected changes in the website’s structure or network issues.
- Optimization: Optimize the script to reduce execution time, possibly by minimizing wait times or using headless browser mode.
- Generalization: Develop a more generalized solution that can adapt to different websites by dynamically identifying login elements.
- Startup Integration: Add the application to the startup programs of the computers so that it runs automatically when the PCs are turned on. This eliminates the need for Veyon Master to run the program simultaneously, making the process more seamless and efficient.

---

## 🏁 **Conclusion**
The Automated Login System for Gunadarma University Wifi Access successfully addressed the inefficiencies of manual login processes in the laboratory. By leveraging Python and Selenium, I was able to create a solution that saved time and effort for the laboratory assistants. However, the project highlighted the importance of flexibility and scalability in automation scripts. With further improvements, such as integrating the application into the startup programs and enhancing its adaptability, this system could be adapted for a wider range of applications, making it a valuable tool for automating repetitive tasks in various environments.

---

## 🛠️ **Dependencies**
To run this project locally, you need to install the following Python dependencies:
- PyInstaller: For converting Python scripts to executables.
  ```bash
  pip install pyinstaller
- Selenium: For browser automation.
  ```bash
  pip install selenium
  
---

## 🤝 **Contributing**
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.

---

## 🙏 **Acknowledgments**
I would like to express my gratitude to Mr. Mahesa, an Elementary Laboratory of Industrial Engineering staff member, for his assistance and support throughout the project. His guidance was instrumental in overcoming challenges and ensuring the project’s success.
