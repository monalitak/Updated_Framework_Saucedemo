import pytest
from selenium import webdriver
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox", help="browser selection")
    parser.addoption("--base_url", action="store", default="https://www.saucedemo.com/", help="base URL")

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "IE":
        driver = webdriver.Ie()

    yield driver
    driver.close()