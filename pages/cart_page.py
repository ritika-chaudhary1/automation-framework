from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    # Locator
    CART_ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    REMOVE_BACKPACK = (
    By.CSS_SELECTOR,
    "[data-test='remove-sauce-labs-backpack']"
)
    # Constructor
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Page Information
    # def get_item_names(self):
    #     items = self.wait.until(
    #         EC.visibility_of_all_elements_located(self.CART_ITEM_NAMES)
    #     )
    #     return [item.text for item in items]

    def get_item_names(self):
       items = self.driver.find_elements(*self.CART_ITEM_NAMES)
       return [item.text for item in items]

    def remove_backpack(self):
      remove_button = self.wait.until(
        EC.element_to_be_clickable(self.REMOVE_BACKPACK)
      )
      remove_button.click()

     # Wait until the product disappears from the cart
      self.wait.until(
        EC.invisibility_of_element_located(self.CART_ITEM_NAMES)
    )  