class loginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_lodin_xpath="//button[normalize-space()='Log in']"
    link_logout_linktext="//a[normalize-space()='Logout']"
    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_lodin_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_linktext).click()
