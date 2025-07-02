from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/CyberPowerPC-i7-14700F-GeForce-Windows-GXiVR8040A17/dp/B0DW48GN42")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

print(f"The price is: {price_dollar}.{price_cents}")

# Closes 1 tab
# driver.close()

# Closes the whole browser
driver.quit()
