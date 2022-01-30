class LoginPage():
    def __init__(self,driver):
        self.driver=driver
        self.username_text_field_id='username'
        self.password_text_field_id ='password'
        self.login_button_id ='Login'
    def enter_username(self,username):
        self.driver.find_element(By.ID,'self.username_text_field_id').send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(By.ID,'self.password_text_field_id').send_keys(password)
    def click_login(self):
        self.driver.find_element(By.ID,'self.login_button_id').click()


