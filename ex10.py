from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\iabba\AppData\Local\Programs\chromedriver_win32(1)\chromedriver.exe")
driver.get("https://jqueryui.com/datepicker/")
fr=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(fr)
driver.find_element(By.ID,"datepicker").click()