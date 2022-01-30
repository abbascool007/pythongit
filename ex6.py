import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\iabba\AppData\Local\Programs\chromedriver_win32(1)\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.bing.com/account/general?")
dd=driver.find_element(By.ID,"rpp")
s=Select(dd)
s.select_by_index(1)

time.sleep(5)
driver.quit()