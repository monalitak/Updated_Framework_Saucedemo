from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver,base_url):
        self.driver = driver
        self.base_url = base_url
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_msg = (By.XPATH,"//h3")

    def login(self, username, password):
        self.driver.get(self.base_url)
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def locked_user(self, username, password):
        self.driver.get(self.base_url)
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        error_msg = self.driver.find_element(*self.error_msg).text
        assert "Sorry, this user has been locked out" in error_msg