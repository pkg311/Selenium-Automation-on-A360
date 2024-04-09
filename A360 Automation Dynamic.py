import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def read_input_file(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            # Split each line by the first colon encountered
            parts = line.strip().split(':', 1)
            if len(parts) == 2:
                key, value = parts
                data[key.strip()] = value.strip()
            else:
                print("Unexpected format in input file:", line)
    return data

def login(driver, username, password, login_url):
    try:
        driver.get(login_url)

        # Wait for the username field to be visible
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]')))

        # Locate password field
        password_field = driver.find_element(By.XPATH, '//input[@name="password"]')

        # Enter username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Click on login button
        login_button = driver.find_element(By.XPATH, '//button[@name="submitLogin"]')
        login_button.click()
    except NoSuchElementException as e:
        print("Element not found during login: ", e)
        raise
    except Exception as e:
        print("An error occurred during login: ", e)
        raise

def fetch_table_data(driver, table_url):
    try:
        # Navigate to the page where the table is located
        time.sleep(3)
        driver.get(table_url)

        # Wait for the table to be visible
        table_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-path="DataTable"]')))
        time.sleep(3)

        # Get all rows of the table
        rows = table_element.find_elements(By.CLASS_NAME, "datatable-row")
        if not rows:
            print("No data found")
            return

        # Iterate over rows and fetch data
        data = []
        for row in rows:
            # Fetching cell data from each row
            cells = row.find_elements(By.CLASS_NAME, "datatable-column-content")
            row_data = [cell.text for cell in cells]
            data.append(row_data)
        return data

    except NoSuchElementException as e:
        print("Element not found during data fetching: ", e)
        raise
    except Exception as e:
        print("An error occurred during data fetching: ", e)
        raise

def MainTest():
    driver = None
    try:
        # Read input data from file
        input_data = read_input_file("Input data file.txt")

        # Create a WebDriver instance
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Perform login using data from input file
        login(driver, input_data['username'], input_data['password'], input_data['login_url'])

        # Fetch table data using data from input file
        data = fetch_table_data(driver, input_data['Table_Inprogress_url'])

        if data:
            for row in data:
                date = row[6]
                if 'Demo Invoice_extractionbot' in row[5]:
                    print('Demo Invoice_extractionbot' + ' started on ' + date)
                    #apply screenshot and mail feature here 
        else:
            print("No data fetched")

    except Exception as e:
        print("An error occurred: ", e)

    finally:
        if driver:
            # Close the WebDriver instance
            driver.quit()

MainTest()
