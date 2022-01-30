import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
s = Service("C:\\Users\\iabba\\Desktop\\chromedriver_win32(1)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.w3schools.com/tags/default.asp")
driver.maximize_window()
time.sleep(15)

a=driver.switch_to.alert
#a.text  #to get the text
#a.send_keys("data")#to enter data into the field
#a.accept() #click on button
#a.dismiss() #cancel the alert

print("a.text")
a.accept()
print("succesfully")

time.sleep(2)
driver.quit()