from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    # Locator
    PRODUCTS_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    PRODUCT_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    FILTER_DROPDOWN = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    PRODUCT_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    ADD_BACKPACK = (
    By.CSS_SELECTOR,
    "[data-test='add-to-cart-sauce-labs-backpack']"
)
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_BUTTON = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

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


    def get_product_names(self):
        products = self.wait.until(
          EC.visibility_of_all_elements_located(self.PRODUCT_NAMES)
        )
        return [product.text for product in products]

    def sort_products(self, option):
        dropdown = self.wait.until(
          EC.element_to_be_clickable(self.FILTER_DROPDOWN)
        )
        Select(dropdown).select_by_value(option)

    def get_product_prices(self):
        price_elements = self.wait.until(
           EC.visibility_of_all_elements_located(self.PRODUCT_PRICES)
        )

        prices = []

        for price in price_elements:
            price_text = price.text.replace("$", "")
            prices.append(float(price_text))

        return prices 

    def add_backpack_to_cart(self):
      add_button = self.wait.until(
        EC.element_to_be_clickable(self.ADD_BACKPACK)
      )
      add_button.click()   


    def get_cart_count(self):
      cart_badge = self.wait.until(
        EC.visibility_of_element_located(self.CART_BADGE)
      )
      return int(cart_badge.text) 


    def click_cart(self):
     cart_button = self.wait.until(
        EC.element_to_be_clickable(self.CART_BUTTON)
      )
     cart_button.click()