import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
s = Service("C:\\Users\\iabba\\Desktop\\chromedriver_win32(1)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.w3schools.com/tags/default.asp")
time.sleep(4)

beforenumber="//tr["
afternumber="]/td[1]"

#beforenumber+2,3,4+afternumber
#2,3,4 should come from for loop
# using _ and giving 2,5 so it runs from 2 to 4
#  _ is a float value so to add with other strings we are using str()
for _ in range(2,5):
    xp1=beforenumber+str(_)+afternumber
    #//tr[2]/td[1]
    #//tr[3]/td[1]
    #tr[4]/td[1]
    value=driver.find_elements(By.XPATH,"xp1").text
    print(value)

time.sleep(2)
driver.quit()