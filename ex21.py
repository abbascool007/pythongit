import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service("C:\\Users\\iabba\\Desktop\\chromedriver_win32(1)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.emirates.com/in/english/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
driver.find_element(By.XPATH,"//a[@data-link='MANAGE']").click()
obj=driver.find_element(By.XPATH,"//a[@data-link='MANAGE:Before you fly']")
ActionChains(driver).move_to_element(obj).perform()

driver.find_element(By.XPATH,"(//div[@aria-level='3']/span[7]").click()


time.sleep(2)
driver.quit()
