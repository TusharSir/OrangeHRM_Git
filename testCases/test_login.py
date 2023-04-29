import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPageClass
from selenium import webdriver

from utilities.readproperties import ReadConfig
from utilities.CustomLogger import LogGenerator


class Test_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGenerator.loggen()


    @pytest.mark.sanity
    @allure.feature('page_title')
    @allure.story('Valid credentials')
    @allure.issue('ABC-123')
    @allure.link(baseUrl, name='Orange HRM Website')
    @allure.title('Test page_title')
    @allure.description('My test description')
    @allure.link('https://www.example.com')
    @allure.severity(allure.severity_level.NORMAL)
    def test_home_page_title(self, setup):
        self.driver = setup
        self.log.info("Test case Started")
        self.log.info(" Test case  Opneing url -->" + self.baseUrl)
        self.driver.get(self.baseUrl)
        self.lg = LoginPageClass(self.driver)
        time.sleep(2)
        self.log.info("Checking logo")
        if self.lg.checkhomepage() == True:
            assert True
            self.log.info("Logo is present")
            self.log.info("Test case is pass")
            self.driver.save_screenshot(".\\Screenshot\\test_home_page_title-pass.png")
            allure.attach(self.driver.get_screenshot_as_png(),name ="Test Page Title-Pass",attachment_type=AttachmentType.PNG)
            self.driver.close()
        else:
            self.log.info("Logo is not present")
            self.log.info("Test case is fail")
            self.driver.save_screenshot(".\\Screenshot\\test_home_page_title-fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="Test Page Title-Pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_login(self, setup):
        self.driver = setup
        self.log.info("Test case Started")
        self.log.info("Opneing url -->" + self.baseUrl)
        self.driver.get(self.baseUrl)
        self.lg = LoginPageClass(self.driver)
        time.sleep(2)
        self.lg.setemail(self.username)
        self.log.info("Enter Username -->" + self.username)
        self.lg.setpassword(self.password)
        self.log.info("password -->" + self.password )
        self.lg.clicklogin()
        self.log.info("Enter login")
        time.sleep(2)
        print(self.lg.checklogin())
        if self.lg.checklogin() == True:
            self.lg.clickmenu()
            self.log.info("click on menu button")
            self.driver.save_screenshot(".\\Screenshot\\test_home_page_title-pass.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Test -pass", attachment_type=AttachmentType.PNG)
            self.lg.clicklogout()
            self.log.info("click on logout button")
            self.log.info("Test case is Pass")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_home_page_title-fail.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Test -fail",
                          attachment_type=AttachmentType.PNG)
            self.log.info("Test case is Fail")
            self.driver.close()
            assert False



