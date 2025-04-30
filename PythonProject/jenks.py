from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Optional: set Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Define the path using Service
service = Service('C:/Users/shilpa.gadiya/Downloads/chromedriverjenkins/chromedriver/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Example usage
driver.get("https://chatgpt.com/")
print(driver.title)
driver.quit()
