import json
import os
import sys

import pytest


from SauceDemo_Framework.pageObjects.login import LoginPage
from SauceDemo_Framework.pageObjects.logout import Logout

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time

base_dir = os.path.dirname(os.path.abspath(__file__))
test_data_path = os.path.abspath(os.path.join(base_dir, '..', 'SauceDemo_Shopping_Framework', 'Data', 'test_data.json'))
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_logout (browserInstance, base_url, test_list_item):
    driver = browserInstance
    loginPage = LoginPage(driver, base_url)
    loginPage.login(test_list_item["userid"], test_list_item["password"])
    logout = Logout(driver)
    logout.logout()
