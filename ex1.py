from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
browser = webdriver.Chrome(executable_path="C:\\Users\iabba\AppData\Local\Programs\chromedriver_win32(1)\chromedriver.exe")
browser.get("https://en.wikipedia.org")
        print(browser.title)
        input=browser.find_element(By id,"searchInput")
        input.send_keys("Python")
        input.send_keys(Keys.ENTER)
        wait=WebDriverWait(browser,10)
        wait.until(EC.presence_of_element_located((By.ID,"content")))
        print(browser.title)
        #print(browser.get_cookies())
        #print(browser.page_source)
        time.sleep(10)
        browser.close()

