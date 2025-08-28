import json
import os
import sys

import pytest

from SauceDemo_Framework.pageObjects.ShopPage import AddtoCart
from SauceDemo_Framework.pageObjects.login import LoginPage
from SauceDemo_Framework.pageObjects.logout import Logout

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time

test_data_path = '../SauceDemo_Framework/Data/test_data.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_delete_product (browserInstance, base_url, test_list_item):
    driver = browserInstance
    driver.implicitly_wait(4)
    loginPage = LoginPage(driver, base_url)
    loginPage.login(test_list_item["userid"], test_list_item["password"])
    shop_page =  AddtoCart(driver)
    shop_page.add_item(test_list_item["product_name"])
    shop_page.goToCart()
    shop_page.delete_product_from_cart(test_list_item["delete_product"])
    logout = Logout(driver)
    logout.logout()
