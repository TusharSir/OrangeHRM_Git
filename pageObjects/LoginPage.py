import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPageClass:

    Text_username_XPATH = (By.XPATH, "//input[@placeholder='Username']")
    Text_Password_XPATH = (By.XPATH, "//input[@placeholder='Password']")
    Btn_Login_XPATH = (By.XPATH, "//button[@type='submit']")
    Click_UserMenu_XPATH = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")
    checklogin_xapth   = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    checkhomepage_xapth  = (By.XPATH, "//img[@alt='company-branding']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        #self.Text_username_XPATH = (By.XPATH, "//input[@placeholder='Username']")

    def setemail(self, email):
        element = self.wait.until(EC.presence_of_element_located(
            self.Text_username_XPATH))
        #self.driver.find_element(self.Text_username_XPATH).clear()
        self.driver.find_element(*LoginPageClass.Text_username_XPATH).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element(*LoginPageClass.Text_Password_XPATH).clear()
        self.driver.find_element(*LoginPageClass.Text_Password_XPATH).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(*LoginPageClass.Btn_Login_XPATH).click()

    def clickmenu(self):
        self.driver.find_element(*LoginPageClass.Click_UserMenu_XPATH).click()

    def clicklogout(self):
        self.driver.find_element(*LoginPageClass.Click_logout_XPATH).click()

    def checkhomepage(self):
        try:
            l = self.driver.find_element(*LoginPageClass.checkhomepage_xapth)
            return True

        except NoSuchElementException:
            return False

    def checklogin(self):
        try:
            l = self.driver.find_element(*LoginPageClass.checklogin_xapth)
            return True

        except NoSuchElementException:
            return False