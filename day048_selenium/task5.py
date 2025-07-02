from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_field = driver.find_element(By.NAME, value="fName")
first_name_field.send_keys("Test")

last_name_field = driver.find_element(By.NAME, value="lName")
last_name_field.send_keys("Test")

email_field = driver.find_element(By.NAME, value="email")
email_field.send_keys("test.test@test.test")

signup_button = driver.find_element(By.TAG_NAME, value="button")
signup_button.click()
