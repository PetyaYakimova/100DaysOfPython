from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_times = [element.text for element in driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")]
event_names = [element.text for element in driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul a")]

all_events = {}
for n in range(len(event_times)):
    all_events[n] = {
        "time": event_times[n],
        "name": event_names[n]
    }

print(all_events)

driver.quit()
