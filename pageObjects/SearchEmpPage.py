import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchEmp:
    Click_EmployeeId_XPATH = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]")
    Click_Search_XPATH = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        #self.Text_username_XPATH = (By.XPATH, "//input[@placeholder='Username']")



    def clickempid(self,empid):
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.Click_EmployeeId_XPATH))
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys(empid)

    def clicksearch(self):
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(
            self.Click_Search_XPATH))
        self.driver.find_element(*SearchEmp.Click_Search_XPATH).click()

    def result(self):
        try:
            time.sleep(1)
            l = self.driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)")
            s=l.text
            #print(s)
            #print("search found")
            return True
        except NoSuchElementException:
            #print("search not found")
            return False

        # m= self.driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").text
        # print(m)

    def searchEmpByName(self):
        flag = False
        for r in range(1,1):
            name = self.driver.find_element(By.CSS_SELECTOR, "b1ody > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(" + str(r) + ") > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").text
            print(name)
        #     if name == Name:
        #         flag = True
        #         #break
        # return flag





