import time

import pytest
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



    # def test_home_page_title(self, setup):
    #     self.driver = setup
    #     self.log.info("Test case Started")
    #     self.log.info(" Test case  Opneing url -->" + self.baseUrl)
    #     self.driver.get(self.baseUrl)
    #     self.lg = LoginPageClass(self.driver)
    #     time.sleep(2)
    #     self.log.info("Checking logo")
    #     if self.lg.checkhomepage() == True:
    #         assert True
    #         self.log.info("Logo is present")
    #         self.log.info("Test case is pass")
    #         self.driver.save_screenshot(".\\Screenshot\\test_home_page_title-pass.png")
    #         self.driver.close()
    #     else:
    #         self.log.info("Logo is not present")
    #         self.log.info("Test case is fail")
    #         self.driver.save_screenshot(".\\Screenshot\\test_home_page_title-fail.png")
    #         self.driver.close()
    #         assert False

    @pytest.mark.test3
    def test_login(self, setup,getdataforlogin):
        self.driver = setup
        self.log.info("Test case Started")
        self.log.info("Opneing url -->" + self.baseUrl)
        self.driver.get(self.baseUrl)
        self.lg = LoginPageClass(self.driver)
        time.sleep(2)
        self.lg.setemail(getdataforlogin[0])
        CheckStauts = []
        self.log.info("Enter Username -->"  + getdataforlogin[0])
        #self.log.info("Enter Username -->" + self.username + getdata[0])
        self.lg.setpassword(getdataforlogin[1])
        self.log.info("password -->" + getdataforlogin[1])
        self.lg.clicklogin()
        self.log.info("Enter login")
        time.sleep(2)
        #print(self.lg.checklogin())
        if self.lg.checklogin() == True:
            if getdataforlogin[2] == "Pass":
                self.lg.clickmenu()
                self.log.info("click on menu button")
                self.driver.save_screenshot(".\\Screenshot\\test_home_page_title-pass.png")
                self.lg.clicklogout()
                self.log.info("click on logout button")
                self.log.info("Test case is Pass")
                self.driver.close()
                CheckStauts.append("Pass")
            elif getdataforlogin[2] == "Fail":
                self.lg.clickmenu()
                self.log.info("click on menu button")
                self.driver.save_screenshot(".\\Screenshot\\test_home_page_title-pass.png")
                self.lg.clicklogout()
                self.log.info("click on logout button")
                self.log.info("Test case is Pass")
                self.driver.close()
                CheckStauts.append("Pass")
        else:
            if getdataforlogin[2] == "Pass":
                self.driver.save_screenshot(".\\Screenshot\\test_home_page_title-fail.png")
                self.log.info("Test case is Fail")
                self.driver.close()
                CheckStauts.append("Fail")
            elif getdataforlogin[2] == "Fail":
                self.driver.save_screenshot(".\\Screenshot\\test_home_page_title-fail.png")
                self.log.info("Test case is Fail")
                self.driver.close()
                CheckStauts.append("Pass")


        print(CheckStauts)
        # if "Fail" not in CheckStauts:
        #     assert True
        #     self.log.info("Parameter Test case is Pass")
        # else:
        #     self.log.info("Parameter Test case is Fail")
        #     assert False




