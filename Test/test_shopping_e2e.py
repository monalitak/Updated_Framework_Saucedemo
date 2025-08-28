import json
import os
import sys

import pytest

from SauceDemo_Framework.pageObjects.ShopPage import AddtoCart
from SauceDemo_Framework.pageObjects.login import LoginPage
from SauceDemo_Framework.pageObjects.logout import Logout
from SauceDemo_Framework.pageObjects.personaldetails_confirmation import purchase

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time

base_dir = os.path.dirname(os.path.abspath(__file__))
test_data_path = os.path.abspath(os.path.join(base_dir, '..', 'SauceDemo_Shopping_Framework', 'Data', 'test_data.json'))
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e_shopping (browserInstance, base_url, test_list_item):
    driver = browserInstance
#    driver.get("https://www.saucedemo.com/")
    loginPage = LoginPage(driver, base_url)
    loginPage.login(test_list_item["userid"], test_list_item["password"])
    shop_page =  AddtoCart(driver)
    shop_page.add_item(test_list_item["product_name"])
    shop_page.goToCart()
    shop_page.checkout()
    final_confirmation = purchase(driver)
    final_confirmation.personal_details()
    final_confirmation.finish()
    logout = Logout(driver)
    logout.logout()
    time.sleep(4)
