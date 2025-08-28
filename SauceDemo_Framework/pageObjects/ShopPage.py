from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddtoCart:
    def __init__(self,driver):
        self.driver = driver
        self.go_to_cart = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")
        self.select_product = (By.XPATH, "//div[@class='inventory_item']")
        #self.delete_from_cart = ()

    def add_item(self, product_name):
        collected_prices = []
        wait = WebDriverWait(self.driver, 10)
        list_item = wait.until(EC.presence_of_all_elements_located((self.select_product)))
        for items in list_item:
            name_item = items.find_element(By.XPATH,".//div[@class='inventory_item_description']/div[@class='inventory_item_label']/a/div[@class='inventory_item_name ']")
            final_item = name_item.text
            print("Product list-:", final_item)
            if final_item in product_name:
                price_elem = items.find_element(By.CLASS_NAME, "inventory_item_price")
                price_text = price_elem.text.replace("$", "")
                price_value = float(price_text)
                collected_prices.append(price_value)
                product = items.find_element(By.CSS_SELECTOR, ".btn_inventory")
                product.click()
                #print(f"Added {final_item} @ {price_value}")
                print("Added product-:", product_name)
        final_amount = sum(collected_prices)
        print("Final price:", final_amount)

    def goToCart(self):
        self.driver.find_element(*self.go_to_cart).click()

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def delete_product_from_cart(self, delete_product):
        product_list = self.driver.find_elements(By.XPATH, "//div[@class='cart_item']")
        for del_product in product_list:
            name = del_product.find_element(By.XPATH,".//div[@class='cart_item_label']/a/div[@class='inventory_item_name']").text
            if name == delete_product:
                remove_id = "remove-" + delete_product.lower().replace(" ", "-")
                del_product.find_element(By.ID, remove_id).click()
                print(f"Removed product -: {delete_product}")
                break
