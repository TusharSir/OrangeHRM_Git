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

from utilities import XLUtils
from utilities.readproperties import ReadConfig
from utilities.CustomLogger import LogGenerator
import string
import random


class Test_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = LogGenerator.loggen()
    path = "D:\\Credence Python Projects by Tushar Sir\\OrangeHRM\\TestData\\EmployeeList.xlsx"

    @pytest.mark.test4
    def test_add_emp(self, setup, random_generator):
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

        time.sleep(4)
        # path = "D:\Credence Python Projects by Tushar Sir\OrangeHRM\TestData\Blue Grayscale Photo Job Vacancy " \
        #        "Announcement (11).png"
        # self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(path)
        time.sleep(4)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.firstname = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.middlename = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lastname = XLUtils.readData(self.path, 'Sheet1', r, 4)
            self.empid = XLUtils.readData(self.path, 'Sheet1', r, 5)
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 6)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 7)
            self.confirmassword = XLUtils.readData(self.path, 'Sheet1', r, 7)
            # time.sleep(2)
            self.ae.clickpim()
            # time.sleep(4)
            self.ae.clickadd()
            self.ae.enterfirstname(self.firstname)
            self.ae.entermiddletname(self.middlename)
            self.ae.enterlastname(self.lastname)
            self.ae.enterempid(self.empid)
            # time.sleep(2)
            self.ae.clickcustomerdetails()
            # self.ae.enterusername("tusharakathalakar1100")
            self.email = random_generator + "@gmail.com"
            # print(self.email)
            self.ae.enterusername(self.username)
            self.ae.enterpassword(self.password)
            self.ae.enterconfrimpassword(self.confirmpassword)
            self.ae.clicksave()

            if self.ae.getsucess() == True:
                lst_status.append("Pass")
            else:
                lst_status.append("Fail")


        print (lst_status)

# def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))
