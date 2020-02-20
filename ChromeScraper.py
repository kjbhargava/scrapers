from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 



#iteration 1:
# 1) go directly to the site
# 2) search for form 
# 3) change dropdown to 460 
# 4) click search 
# 5) change drop down column for date to get most recent data 
# 6) search for last name of __insertcandidatename___ 
# 7) if candidatename matches dictionary then click on excel download button 
# 8) repeat for every excel sheet with candidate name in the page for the year
# 9) if no more place then check and see if you are still in the right year
# 10) if you are then navigate to the next page 
# 11) repeat step 6-10 until you get to end of page numbers or end of year

driver = webdriver.Chrome()

#step 1
driver.get("https://www.python.org")
try:
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "barWrap-toggle"))
        
    )
finally:
    driver.quit() 
# assert "Python" in driver.title
# print(driver.title)
# elem = driver.find_element_by_name("q") 
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close() 