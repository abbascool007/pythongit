import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service("C:\\Users\\iabba\\Desktop\\chromedriver_win32(1)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://login.salesforce.com")
driver.maximize_window()
driver.find_element(By.ID,"username").send_keys("Abbas")
driver.find_element(By.ID,"password").send_keys("abz@123")
driver.find_element(By.ID,"login").click()
#giving extra time to login into the account
time.sleep(40)
#once entered to the site clicking on the values as per demo clicking on object 'create' and 'user'.
driver.find_element(By.XPATH,"").click()
driver.find_element(By.XPATH,"").click()
#giving extra time to load page
time.sleep(8)

#since the page & site has multiple separate frames, first we are switching into the desired frame. 'frame1' bcz it has multiple frames
frame1=driver.find_element(By.XPATH,"")
driver.switch_to.frame(frame1)

#to enter values in the objects
driver.find_element(By.ID,"").send_keys("mobile")
#to click on magnifying window and it will open a new window
driver.find_element(By.XPATH,"").click()
time.sleep(5)

#to movw to the new opened window we need to use window_handles command. we have to use the index id of the windows like 0,1
#first will capture the info of 'user' window & second will do for new pop up window
first=driver.window_handles[0]
second=driver.window_handles[1]
#to switch to the new window
driver.switch_to.window(second)
#we found in html code that it is also in frames so we are using frame2 and after that switching to new window
frame2=driver.find_element(By.ID,"")
driver.switch_to.frame(frame2)
#entering value in the new window
driver.find_element(By.ID,"").send_keys("abbas")
#to do search operation
driver.find_element(By.name,"").click()

#once we are done with the new window operations if we want to move back to normal window
driver.switch_to.window(first)

time.sleep(5)
driver.quit()