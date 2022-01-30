import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\iabba\AppData\Local\Programs\chromedriver_win32(1)\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.bing.com/")
driver.find_element(By.ID,"sb_form_q").send_keys("amazon")
driver.find_element(By.ID,"search_icon").click()

time.sleep(5)
driver.quit()


