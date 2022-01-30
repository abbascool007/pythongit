import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\iabba\AppData\Local\Programs\chromedriver_win32(1)\chromedriver.exe")
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
time.sleep(2)
fr=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(fr)

src=driver.find_element(By.ID,"draggable")
dest=driver.find_element(By.ID,"droppable")
ActionChains(driver).drag_and_drop(src,dest).perform()

time.sleep(5)
driver.quit()