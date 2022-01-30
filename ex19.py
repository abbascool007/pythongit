import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:/Users/iabba/Desktop/chromedriver_win32(1)/chromedriver.exe")
driver.get("https://www.emirates.com/in/english/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[@data-link='MANAGE']").click()
obj=driver.find_element(By.XPATH,"//a[@data-link='MANAGE:Before you fly']")

ActionChains(driver).move_to_element(obj).perform()

time.sleep(2)
driver.quit()