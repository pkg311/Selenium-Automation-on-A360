import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException

# from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.maximize_window()
# def setup():
#     option = Options()
#     option.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=option)
#     yield driver
#     driver.quit()

def login(driver):
    try:
        driver.get("https://community.cloud.automationanywhere.digital/#/login?")

        # Locate username and password fields
        username_field = driver.find_element(By.XPATH, '//input[@name="username"]')
        password_field = driver.find_element(By.XPATH, '//input[@name="password"]')

        # Enter username and password
        username_field.send_keys("praveenkumar.gaurav@adani.com")
        password_field.send_keys("Ga1999av@")

        # Click on login button
        login_button = driver.find_element(By.XPATH, '//button[@name="submitLogin"]')
        login_button.click()
    except NoSuchElementException as e:
        print("Element not found: ", e)
    except Exception as e:
        print("An error occurred during login: ", e)


def fetch_table_data(driver):
    # Navigate to the page where the table is located
    time.sleep(6)
    driver.get("https://community.cloud.automationanywhere.digital/#/activity/inprogress")
    time.sleep(6)
    # Locate the table element
    table_element = driver.find_element(By.XPATH, '//div[@class="datatable datatable--with-actions datatable--theme-landing"]')
    time.sleep(60)
    print(table_element.text)

    # Get all rows of the table
    rows = table_element.find_elements(By.TAG_NAME, "tr")
    # #
    data = []
    # Iterate over rows and fetch data
    for row in rows:  # Exclude the header row
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]
        print(cells[2].text)
        cells[2].click()
        data.append(row_data)
        time.sleep(6)






# driver = setup()  # Note the parentheses to invoke the function and get the driver instance

login(driver)  # Passing the driver instance to login
# data="hello"
fetch_table_data(driver)
# print(data)