import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\iabba\AppData\Local\Programs\chromedriver_win32(1)\chromedriver.exe")
driver.maximize_window()
driver.get("https://jqueryui.com/tooltip/") 
time.sleep(2)
fr=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(fr)
obj=driver.find_element(By.ID,"age")
p1=obj.get_attribute("title")
print("tool tip message is :" +p1)