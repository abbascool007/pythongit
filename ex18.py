import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\iabba\AppData\Local\Programs\chromedriver_win32(1)\chromedriver.exe")
driver.get("https://www.bing.com/")
driver.maximize_window()
driver.find_element(By.ID,"sb_form_q").send_keys("surendra")
time.sleep(2)

p1=driver.find_elements(By.XPATH,"//Li[@class='sa_sg']")

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)

driver.get_screenshot_as_file("C:/Users/iabba/AppData/Local/Programs/scrn1.png")

time.sleep(2)
driver.quit()