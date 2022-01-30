import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C:\\Users\\iabba\\Desktop\\chromedriver_win32(1)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
time.sleep(2)

driver.execute_script("window.location='http://www.bing.com'")
driver.execute_script("document.getElementById('sb_form_q').value='surendra jaganadam'")
driver.execute_script("document.getElementById('sb_form_go').click();")

time.sleep(2)
driver.quit()