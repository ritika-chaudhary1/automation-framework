from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Actions
    def enter_username(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()

    def get_error_message(self):
       error_message = self.wait.until(
        EC.visibility_of_element_located(self.ERROR_MESSAGE)
       )
       return error_message.text    