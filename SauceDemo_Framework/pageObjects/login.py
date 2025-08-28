from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.driver.implicitly_wait(4)
        try:
        error_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3"))
        )
        return error_element.text
    except Exception as e:
        self.driver.save_screenshot("locked_user_failure.png")
        raise e
        
