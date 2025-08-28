from selenium.webdriver.common.by import By


class Logout:
    def __init__(self,driver):
        self.driver = driver
        self.left_slider = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")

    def logout(self):
        self.driver.find_element(*self.left_slider).click()
        self.driver.find_element(*self.logout_button).click()