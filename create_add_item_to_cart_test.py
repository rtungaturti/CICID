Here is an example of Selenium test code for creating an "Add Item to Cart" feature:
```
# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the test environment
driver = webdriver.Chrome()  # Replace with your preferred browser
driver.get("https://example.com")  # Replace with your website URL

# Find the product item element
product_item = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item"))
)

# Click on the "Add to Cart"
add_to_cart_button = product_item.find_element_by_css_selector(".add-to-cart-button")
add_to_cart_button.click()

# Verify the item is added to cart
cart_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-icon"))
)
assert cart_icon.text == "1 item in cart"

# Clean up
driver.quit()
```
Note: This code assumes a basic HTML structure for the product item element, and you may need to adjust the CSS selectors to match your specific HTML structure. Additionally, you may want to add more assertions or verification steps to ensure the test is comprehensive.