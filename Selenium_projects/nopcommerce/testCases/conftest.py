from selenium import webdriver
from utilities.utility import *
from utilities.readProperties import readConfig
from utilities.nopCommerceLogger import LogGeneration
import pytest

logger = LogGeneration.loggen()

@pytest.fixture
def setup(browser):
    if browser == "chrome":
        logger.info("Running test on Chrome browser")
        driver = webdriver.Chrome("{0}".format(readConfig.chrome_driver_path()))
    elif browser == "firefox":
        logger.info("Running test on firefox browser")
        driver = webdriver.Firefox("{0}".format(readConfig.chrome_driver_path()))
    else:
        driver = webdriver.Chrome("{0}".format(readConfig.chrome_driver_path()))
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

