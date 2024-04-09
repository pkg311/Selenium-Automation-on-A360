# Selenium-Automation-on-A360

**Project Manual: Automation for Table Data Retrieval**

**1. Prerequisite:**

- Python 3.x environment set up.
- Required packages installed using pip or conda.
- ChromeDriver installed and accessible from the system's PATH.
- Input data file containing login credentials and URLs.

**2. Requirement Impact Explanation:**

This project aims to automate the retrieval of table data from a web application. The impact of this automation includes:
- Time-saving: Manual data retrieval can be time-consuming. Automating the process reduces the time spent on repetitive tasks.
- Accuracy: Human errors in data entry are eliminated, ensuring accurate data retrieval.
- Scalability: The automation script can be easily adapted to fetch data from different tables or sources with minimal changes.
- Consistency: Automated scripts perform tasks consistently, reducing variability in data retrieval.

**3. Manual:**

**3.1. Setting up Environment:**

- Ensure Python 3.x is installed.
- Install required packages listed in the dependencies section using `pip install <package>` or `conda install <package>`.
- Download ChromeDriver and place it in a directory accessible from the system's PATH.

**3.2. Input Data File:**

Create a text file (`input_data.txt`) with the following format:
```
username: <your_username>
password: <your_password>
login_url: <login_page_url>
Table_Inprogress_url: <table_page_url>
```

**3.3. Running the Script:**

- Execute `run.bat` to activate the virtual environment and run the Python script.
- Alternatively, run the Python script directly using `python script_name.py`.

**3.4. Scheduled Execution:**

- Add `run.bat` as a new task in Windows Task Scheduler to execute the script at scheduled times.

**3.5. Script Explanation:**

The Python script automates the following tasks:
- Reading input data from the input file.
- Initializing a Chrome WebDriver.
- Logging in to the web application using provided credentials.
- Navigating to the page containing the table.
- Fetching table data and storing it for further processing.

**3.6. Code Explanation:**

- `read_input_file(filename)`: Reads input data from a text file and returns it as a dictionary.
- `login(driver, username, password, login_url)`: Automates the login process using provided credentials.
- `fetch_table_data(driver, table_url)`: Fetches table data from the specified URL.
- `MainTest()`: Main function to execute the automation tasks.
- `run.bat`: Batch file to activate the virtual environment and run the Python script.

**4. Dependencies:**

List of required Python packages and their versions:
- attrs==23.1.0
- certifi==2023.11.17
- cffi==1.16.0
- charset-normalizer==3.3.2
- chromedrivermanager==0.0.1
- colorama==0.4.6
- exceptiongroup==1.2.0
- h11==0.14.0
- idna==3.6
- iniconfig==2.0.0
- Jinja2==3.1.2
- MarkupSafe==2.1.3
- outcome==1.3.0.post0
- packaging==23.2
- pluggy==1.3.0
- pycparser==2.21
- pypiwin32==223
- PySocks==1.7.1
- pytest==7.4.3
- pytest-html==4.1.1
- pytest-metadata==3.0.0
- pywin32==306
- requests==2.31.0
- selenium==4.16.0
- sniffio==1.3.0
- sortedcontainers==2.4.0
- tomli==2.0.1
- trio==0.23.2
- trio-websocket==0.11.1
- urllib3==2.1.0
- wsproto==1.2.0

**Note:** Ensure to keep the dependencies updated as per the project requirements.

This manual provides a comprehensive guide for setting up, running, and scheduling the automation script for table data retrieval. It also includes explanations of code functionality and dependency management for the project.
