from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome browser (make sure you have Chrome installed)
driver = webdriver.Chrome()

# Open Google
driver.get("https://lda-services-stag.e-connectsolutions.com/#/login")

# Wait for 2 seconds
time.sleep(2)

# Find the search box, type a query, and press Enter
search_box = driver.find_element(By.ID, "LoginId")
search_box.send_keys("deepy10796")
search_box.submit()

# Wait a bit and close the browser
time.sleep(3)
driver.quit()
