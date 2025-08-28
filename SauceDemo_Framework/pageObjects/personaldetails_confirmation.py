from selenium.webdriver.common.by import By

class purchase:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.summary_subtotal = (By.XPATH, "//div[@class='summary_subtotal_label']")
        self.confirmation_message = (By.XPATH, "//h2")

    def personal_details(self):
        self.driver.find_element(*self.first_name).send_keys("t")
        self.driver.find_element(*self.last_name).send_keys("t")
        self.driver.find_element(*self.postal_code).send_keys("t")
        self.driver.find_element(*self.continue_button).click()

    def finish(self):
        self.driver.find_element(*self.finish_button).click()

    def total_price(self):
        Item_total = self.driver.find_element(*self.summary_subtotal).text
        checkout_amount = float(Item_total.replace("Item total: $", ""))
        print(checkout_amount)
        confirmation_message = self.driver.find_element(*self.confirmation_message).text
        assert "Thank you" in confirmation_message