import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\iabba\AppData\Local\Programs\chromedriver_win32(1)\chromedriver.exe")
driver.maximize_window()
driver.get("https://jqueryui.com/resizable/")
time.sleep(2)
fr=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(fr)
obj=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-e']")
ActionChains(driver).drag_and_drop_by_offset(obj,100,100).perform()
obj2=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-s']")
ActionChains(driver).drag_and_drop_by_offset(obj2,150,150).perform()

time.sleep(5)
driver.quit()