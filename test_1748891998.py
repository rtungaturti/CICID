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
username = driver.find_element_by_id("username")
username@example.com"
username.send_keys("username@example.com")

# Enter password
password = driver.find_element_by_id("password")
password.send_keys("password123")

# Click the login button
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

# Wait for the login to be successful
WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
```
Note: Replace the `https://example.com` with your actual login page and `username@example.com` and `password123` with your actual login credentials.