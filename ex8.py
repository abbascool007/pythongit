from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\iabba\AppData\Local\Programs\chromedriver_win32(1)\chromedriver.exe")
driver.get("https://developer.salesforce.com/signup")

obj=driver.find_elements(By.NAME,"job_role")
p1=obj.find_elements(By.TAG_NAME,"option")

print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)