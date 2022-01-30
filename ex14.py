import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\iabba\AppData\Local\Programs\chromedriver_win32(1)\chromedriver.exe")
driver.maximize_window()
driver.get("https://jqueryui.com/draggable/")
time.sleep(3)

fr=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(fr)
obj=driver.find_element(By.ID,"draggable")
s=obj.size
l=obj.location
print(obj.get_attribute("class"))

print(s)
print(l)