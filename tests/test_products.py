from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_products_are_displayed(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Products page
    products_page = ProductsPage(driver)

    product_names = products_page.get_product_names()

    assert len(product_names) > 0


def test_sort_products_low_to_high(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Products page
    products_page = ProductsPage(driver)

    # Select Price (low to high)
    products_page.sort_products("lohi")

    # Get product prices
    prices = products_page.get_product_prices()

    # Verify prices are sorted from low to high
    assert prices == sorted(prices)

   # Verify product names are sorted accordingly a to z
    
def test_sort_products_name_a_to_z(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Products page
    products_page = ProductsPage(driver)

    # Select Name (A to Z)
    products_page.sort_products("az")

    # Get product names
    product_names = products_page.get_product_names()

    # Verify names are sorted A to Z
    assert product_names == sorted(product_names)



def test_sort_products_name_z_to_a(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Products page
    products_page = ProductsPage(driver)

    # Select Name (Z to A)
    products_page.sort_products("za")

    # Get product names
    product_names = products_page.get_product_names()

    # Verify names are sorted Z to A
    assert product_names == sorted(product_names, reverse=True)


def test_sort_products_high_to_low(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Products page
    products_page = ProductsPage(driver)

    # Select Price (high to low)
    products_page.sort_products("hilo")

    # Get product prices
    prices = products_page.get_product_prices()

    # Verify prices are sorted from high to low
    assert prices == sorted(prices, reverse=True)


    #for the test case to add backpack to cart
def test_add_product_to_cart(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Products page
    products_page = ProductsPage(driver)

    # Add Backpack to cart
    products_page.add_backpack_to_cart()

    # Verify cart count
    assert products_page.get_cart_count() == 1


def test_product_appears_in_cart(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Products page
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()
    products_page.click_cart()

    # Cart page
    cart_page = CartPage(driver)

    item_names = cart_page.get_item_names()

    assert "Sauce Labs Backpack" in item_names


def test_remove_product_from_cart(driver):

    driver.get("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Products page
    products_page = ProductsPage(driver)

    products_page.add_backpack_to_cart()
    products_page.click_cart()

    # Cart page
    cart_page = CartPage(driver)

    # Remove Backpack
    cart_page.remove_backpack()

    # Verify product is removed
    item_names = cart_page.get_item_names()

    assert "Sauce Labs Backpack" not in item_names    