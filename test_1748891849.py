Here is the Selenium test code for login:
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://example.com/login")

# Enter username
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username_input.send_keys("your_username")

# Enter password
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_input.send_keys("your_password")

# Click the login button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login_button"))
)
login_button.click()
```
Note: Replace `https://example.com/login` with the actual URL of your login page, and `your_username` and `your_password` with your actual login credentials.