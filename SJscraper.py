from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.ui import Select
import time
import random 

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
waiting = driver.implicitly_wait(random.randint(1,6))

random.randint(1,6)
#step 1 go directly to the site (other scraper was going to a different page)
driver.get("https://www.southtechhosting.com/SanJoseCity/CampaignDocsWebRetrieval/Search/SearchByFiledForm.aspx")
try:
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'ctl00_DefaultContent_ASPxRoundPanel1_ASPxDDL_Forms_B-1')))
except TimeoutException:
    print("Loading took too long.")

# driver.implicitly_wait(10)
elem2= driver.find_element(By.ID, 'ctl00_DefaultContent_ASPxRoundPanel1_ASPxDDL_Forms_I') 

#get to the dropdown menu and press the down arrow key until you get to the forms you want and then press return to search for them
for x in range(0,18):
    elem2.send_keys(Keys.DOWN)
elem2.send_keys(Keys.RETURN)

#tell the script to wait a few seconds so the website doesn't intercept a click and kill the program
time.sleep(8)

#click on the column for date to order the sheets by most recent
column_filter = driver.find_element(By.ID, 'ctl00_GridContent_gridFilers_col1')
column_filter.click()

#start a series of conditionals checking whether the candidate is there or not and then downloading the file

#first test file download
fileName = driver.find_elements_by_xpath('//a[@class="dxbButton_Glass dxgvCommandColumnItem_Glass dxgv__cci dxbButtonSys"]')
fileName.click()

xpath='//td[@class="dxgvCommandColumn_Glass dxgv"

#BIG FIND! Each Id tag for the excel and pdf files is numerically listed from 0-18 
#it repeats on each page so the first pdf ends in tn0, the first excel ends in tn1
#2nd pdf ends in tn2, 2nd excel ends in tn3....until it gets to tn18...then when you click
#on the next page it restarts the IDs from 0-18 again! So now in theory, we don't need to download
#every single pdf and excel file.  We just need to download the id's of the ones that
#have a first and last name in the <td> element

#class name for anchor
#dxbButton_Glass dxgvCommandColumnItem_Glass dxgv__cci dxbButtonSys

#dxbButton_Glass dxgvCommandColumnItem_Glass dxgv__cci dxbButtonSys

#id name for anchor
#ctl00_GridContent_gridFilers_DXCBtn13
#ctl00_GridContent_gridFilers_DXCBtn3