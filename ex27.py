import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
s = Service("C:\\Users\\iabba\\Desktop\\chromedriver_win32(1)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.w3schools.com/tags/default.asp")
time.sleep(4)

driver.find_element(By.XPATH,"//table[@class='ws-table-all notranslate']/tbody")
tablerow=driver.find_elements(By.TAG_NAME,"tr")
print(len(tablerow))