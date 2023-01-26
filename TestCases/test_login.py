import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from pageObjects.loginPage import loginPage
from Utilities.readProperties import ReadConfig
from Utilities.costomLogger import logGen

class Test_001_login:
    BaseUrl= ReadConfig.getApplicatinURL()
    username=ReadConfig.getuserMail()
    password=ReadConfig.getuserPassword()
    logger=logGen.loggen()


    def test_homePageTitle(self,setup):
        self.logger.info("*********** Test_001_login**********")
        self.logger.info("***** verify homePage ******")
        self.driver=setup
        self.driver.get(self.BaseUrl)
        driver.maximize_window()
        time.sleep(5)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***** homPage title test case is pass *****")
        else:
            self.driver.save_screenshot(".\\Sceenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.info("***** homPage title test case is Fail *****")
            assert False

    def test_login(self,setup):
        self.logger.info("***** verify login ******")
        self.driver=setup
        self.driver.get(self.BaseUrl)
        driver.maximize_window()
        time.sleep(5)
        self.lp=loginPage(self.driver)
        time.sleep(2)
        self.lp.setUsername(self.username)
        time.sleep(2)
        self.lp.setPassword(self.password)
        time.sleep(2)
        self.lp.clicklogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("***** homPage title test case is pass *****")
        else:
            self.driver.save_screenshot(".\\Sceenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.info("***** homPage title test case is Fail *****")
            assert False
        driver.quit()