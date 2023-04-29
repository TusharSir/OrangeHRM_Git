import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--ignore-certificate-errors")

# service_obj = Service()

#
# class test_OrangeHRM:
#     def test_Login(self):

driver = webdriver.Firefox()
driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#wait = WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
Homepage = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//img[@alt='company-branding']")))
driver.save_screenshot("HomePage.png")
print(driver.title)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Tushar")
driver.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys("A")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Kathalkar")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]").clear()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]").send_keys("101")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
AddEmp = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//h6[normalize-space()='Personal Details']")))
driver.save_screenshot("Addemp.png")
driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("Alice")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("searchemp.png")

driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
print("Test pass")

#try except block
# try:
#     l = driver.find_element(By.XPATH, "//h1[@class='display-4 mb-0']")
#     s= l.text
#     print("Element exist -" + s)
#     #NoSuchElementException thrown if not present
# except NoSuchElementException:
#     print("Element does not exist")

time.sleep(5)

#driver.find_element(By.CSS_SELECTOR, "button[id='dropdownMenuProfile'] i[class='material-icons']").click()

# try:
#     l = driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']")
#     s = l.text
#     print("Element exist -" + s)
#     # NoSuchElementException thrown if not present
#     driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
#     driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
#     print("Test pass")
# except NoSuchElementException:
#     print("Element does not exist")
#     print("Test Fail")
#
# wait = WebDriverWait(driver, 20)
#
# w= wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[id='dropdownMenuProfile'] i[class='material-icons']")))
# print(w)
# driver.find_element(By.CSS_SELECTOR,"button[id='dropdownMenuProfile'] i[class='material-icons']").click()
# #time.sleep(5)
#
# driver.find_element(By.XPATH, "//div[normalize-space()='Logout']").click()

