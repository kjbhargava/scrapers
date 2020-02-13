from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.python.org")

assert "Python" in driver.title
print(driver.title)
elem = driver.find_element_by_name("q") 