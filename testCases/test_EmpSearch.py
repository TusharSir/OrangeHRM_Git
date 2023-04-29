import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.AddEmployee import AddEmpClass
from pageObjects.LoginPage import LoginPageClass
from selenium import webdriver

from pageObjects.SearchEmpPage import SearchEmp
from utilities.readproperties import ReadConfig
from utilities.CustomLogger import LogGenerator
import string
import random


class Test_EmpSearch:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_emp_search(self, setup, random_generator):
        self.driver = setup
        self.log.info("Test case Started")
        self.log.info(" Test case  Opneing url -->" + self.baseUrl)
        self.driver.get(self.baseUrl)
        self.lg = LoginPageClass(self.driver)
        # time.sleep(2)
        self.lg.setemail(self.username)
        self.log.info("Enter Username -->" + self.username)
        self.lg.setpassword(self.password)
        self.log.info("password -->" + self.password)
        self.lg.clicklogin()
        self.log.info("Enter login")
        self.ae = AddEmpClass(self.driver)
        self.ae.clickpim()
        self.log.info("Click on Pim")
        self.es = SearchEmp(self.driver)
        self.es.clickempid("0221")
        self.es.clicksearch()
        print(self.es.result())
        if print(self.es.result()) == True:
            self.log.info("empid is present")
            self.log.info("Test case is pass")
            assert True
        else:
            self.log.info("empid is not present")
            self.log.info("Test case is fail")
            assert False
