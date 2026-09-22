from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    # Locator
    PRODUCTS_TITLE = (By.CSS_SELECTOR, "[data-test='title']")

    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Page Information
    def get_title(self):
        title = self.wait.until(
            EC.visibility_of_element_located(self.PRODUCTS_TITLE)
        )
        return title.text