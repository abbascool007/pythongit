import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import HtmlTestRunner
from pageobjectmodel.pages.LoginPage import LoginPageProp
from pageobjectmodel.pages.Homepage import HomePageProp
from pageobjectmodel.pages.CreateUserPage import CreateUserProp

#   from webdriver_manager.chrome import ChromeDriverManager - we have to import this if we use the below for driver call
# cls.driver=webdriver.Chrome(ChromeDriverManager().install())


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        s = Service("C:\\Users\\iabba\\Desktop\\chromedriver_win32(1)\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
#we can use " cls.driver=webdriver.Chrome(ChromeDriverManager().install()) " instead of the above driver call

        cls.driver.get("https://login.salesforce.com")
        cls.driver.maximize_window()
#using extra 'a' to perform the operation in order so it will 1st do 'a' then 'b' and go on
    def test_a_login(self):
        driver=self.driver
        Login=LoginPage(driver)
        login.enter_username("Abbas")
#using defined loginProp to call all property values
        #self.driver.find_element(By.ID,LoginProp.username_text_field_id).send_keys("Abbas")
        #self.driver.find_element(By.ID,LoginProp.password_text_field_id).send_keys("abz@123")
        #self.driver.find_element(By.ID,LoginProp.login_button_id).click()
        time.sleep(35)

    def test_b_createUser(self):
        homePage=HomePageProp()
        #once entered to the site clicking on the values as per demo clicking on object 'create' and 'user'.
        self.driver.find_element(By.XPATH,'homePage.Create_button_xpath').click()
        self.driver.find_element(By.XPATH,'homePage.Create_user_xpath').click()
        # giving extra time to load page
        time.sleep(8)
        createUser=CreateUserProp()

        # since the page & site has multiple separate frames, first we are switching into the desired frame. 'frame1' bcz it has multiple frames
        frame1 = self.driver.find_element(By.XPATH,'createUser.Create_User_new_frame_xpath')
        self.driver.switch_to.frame(frame1)
        self.driver.find_element(By.ID,'createUser.firstname_id').send_keys("mobile")

    @classmethod
    def teatDownClass(cls):
        time.sleep(5)
        cls.driver.quit()


if __name__ == '__main__':
#to pass multiple parameters we are using verbosity and giving 2 as value
# here we are replacing this command with the blow commad   "  unittest.main(verbosity=2)  "
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/iabba/PycharmProjects/pythonProject2/reports'),verbosity=2)

