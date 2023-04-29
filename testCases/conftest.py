import openpyxl
import pytest
from selenium import webdriver
import datetime
import string
import random
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
import pytest
import pandas as pd
from pytest_excel import pytest_excel


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("headless")
        service_obj = Service()
        #driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        driver = webdriver.Chrome()
        print("launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching chrome browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("launching chrome browser")
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
#        driver = webdriver.Firefox()
        print("launching chrome browser")
    driver.maximize_window()
    # yield
    # driver.quit()
    return driver


def pytest_configure(config):
    config._metadata['Project Name'] = 'Oranghm'
    config._metadata['Module Name'] = 'Employee'
    config._metadata['Tester'] = 'Credence'


@pytest.fixture(params=[
    ("Admin", "admin123", "Pass"),
    ("Admin", "admin1232", "Fail"),
    ("Admin1", "admin123", "Fail"),
    ("Admin1", "admin1232", "Fail")
])
def getdataforlogin(request):
    return request.param


@pytest.fixture(params=[
    ("Aishwarya", "Vinamra", "Patil", "1021", "Aishwarya123@credence.com", "AishwaryaQq@12345"),
        ("Harshal", "Balu", "Gharate", "1021", "Harshal23@credence.com", "HarshalQq@12345"),
        ("Pranav", "Kanipnath", "Patil", "1021", "Pranav13@credence.com", "PranavQq@12345"),
        ("Akshada", "Vilas", "Thopte", "1021", "Akshada123@credence.com", "AkshadaQq@12345"),
        ("Yaseen", "Dastagir", "Syed", "1021", "Yaseen123@credence.com", "YaseenQq@12345")

])
def getdataforaddemp(request):
    return request.param


# @pytest.fixture
# def getdataforaddemp(request):
#     return pd.read_excel('D:\\Credence Python Projects by Tushar Sir\\OrangeHRM\\TestData\\EmployeeList.xlsx', sheet_name='Sheet1')
#

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, ''
#                                 '')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#         driver.get_screenshot_as_file(name)


# @pytest.mark.parametrize("username, password, expected", [
#         ("Admin", "admin123", "Pass"),
#         ("Admin", "admin1232", "Fail"),
#         ("Admin1", "admin123", "Fail"),
#         ("Admin1", "admin1232", "Fail")])
