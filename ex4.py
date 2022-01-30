import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\iabba\AppData\Local\Programs\chromedriver_win32(1)\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.bing.com/account/general?")
p1=driver.find_element(By.ID,"enAS").is_selected()
print(p1)
if p1:
    print("already checked")
else:
    driver.find_element(By.ID,"enAS").click()
    print("successfully checked")

time.sleep(5)
driver.quit()