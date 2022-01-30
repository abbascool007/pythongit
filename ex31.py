import xlrd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\\Users\\iabba\\Desktop\\chromedriver_win32(1)\\chromedriver.exe")
driver.get("https://www.bing.com")
driver.maximize_window()
time.sleep(2)

loc=("C:/Users/iabba/Desktop/PI samples/datadriven.xlsx")
wb = xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
p1=sheet.cell(0,0).value
print(p1)
#to get tot no of rows and columns
print(sheet.nrows)
print(sheet.ncols)
#to get all row values
for i in range(sheet.nrows):
    p2 = sheet.cell(i,0).value
    print(p2)
#o/p will be all row values from first to last
    driver.find_element(By.ID,"sb_form_q").clear()
    driver.find_element(By.ID,"sb_form_q").send_keys(p2)
    time.sleep(2)
#here we are opening the brower app and entering values one by one from excell rows with time interval.
#"clear()" is used to clear each and every time after the value entered so that next value can be searched.
time.sleep(5)
driver.quit()
