import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddEmpClass:
    Click_PIM_XPATH = (By.XPATH, "//span[normalize-space()='PIM']")
    Click_Add_XPATH = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]/i[1]")
    Text_FirstName_XPATH = (By.XPATH, "//input[@placeholder='First Name']")
    Text_MiddleName_XPATH = (By.XPATH, "//input[@placeholder='Middle Name']")
    Text_LastName_XPATH = (By.XPATH, "//input[@placeholder='Last Name']")
    Text_EmpId_XPATH = (By.XPATH,
                        "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div["
                        "2]/div[1]/div[1]/div[2]/input[1]")
    Btn_Create_Login_Details_XPATH = (
        By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
    Text_Username_XPATH = (By.XPATH,
                           "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div["
                           "3]/div[1]/div[1]/div[1]/div[2]/input[1]")
    Text_password_XPATH = (By.XPATH,
                           "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div["
                           "4]/div[1]/div[1]/div[1]/div[2]/input[1]")
    Text_confrimpassword_XPATH = (By.XPATH,
                                  "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div["
                                  "2]/div[4]/div[1]/div[2]/div[1]/div[2]/input[1]")
    Btn_Save_XPATH = (By.XPATH, "//button[@type='submit']")
    sucessmessage = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def clickpim(self):
        self.wait.until(EC.presence_of_element_located(
            self.Click_PIM_XPATH))
        self.driver.find_element(*AddEmpClass.Click_PIM_XPATH).click()

    def clickadd(self):
        self.wait.until(EC.presence_of_element_located(
            self.Click_Add_XPATH))
        self.driver.find_element(*AddEmpClass.Click_Add_XPATH).click()

    def enterfirstname(self, firstname):
        self.wait.until(EC.presence_of_element_located(
            self.Text_FirstName_XPATH))
        self.driver.find_element(*AddEmpClass.Text_FirstName_XPATH).clear()
        self.driver.find_element(*AddEmpClass.Text_FirstName_XPATH).send_keys(firstname)

    def entermiddletname(self, middletname):
        self.driver.find_element(*AddEmpClass.Text_MiddleName_XPATH).clear()
        self.driver.find_element(*AddEmpClass.Text_MiddleName_XPATH).send_keys(middletname)

    def enterlastname(self, lastname):
        self.driver.find_element(*AddEmpClass.Text_LastName_XPATH).clear()
        self.driver.find_element(*AddEmpClass.Text_LastName_XPATH).send_keys(lastname)

    def enterempid(self, empid):
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(
            (self.Text_EmpId_XPATH)))
        self.driver.find_element(*AddEmpClass.Text_EmpId_XPATH).clear()
        self.driver.find_element(*AddEmpClass.Text_EmpId_XPATH).send_keys(empid)

    def clickcustomerdetails(self):
        self.driver.find_element(*AddEmpClass.Btn_Create_Login_Details_XPATH).click()

    def enterusername(self, username):
        self.driver.find_element(*AddEmpClass.Text_Username_XPATH).clear()
        self.driver.find_element(*AddEmpClass.Text_Username_XPATH).send_keys(username)

    def enterpassword(self, password):
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div["
                                           "1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]").clear()
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div["
                                           "1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys(password)

    def enterconfrimpassword(self, confrimpassword):
        self.driver.find_element(*AddEmpClass.Text_confrimpassword_XPATH).clear()
        self.driver.find_element(*AddEmpClass.Text_confrimpassword_XPATH).send_keys(confrimpassword)

    def clicksave(self):
        self.driver.find_element(*AddEmpClass.Btn_Save_XPATH).click()

    def getsucess(self):
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/p[2]")
            l = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(
                (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[2]/p[2]")))
            # s = l.text
            # print(s)
            # print("Element does exist")
            return True

            # NoSuchElementException thrown if not present
        except NoSuchElementException:
            # print("Element does not exist")
            return False
