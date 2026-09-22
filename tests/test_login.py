from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_valid_login(driver):

    driver.get("https://www.saucedemo.com/")

#login
    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Verify Products page
    products_page = ProductsPage(driver)

    assert products_page.get_title() == "Products"


    #test inavlid login
def test_invalid_login(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    error_message = login_page.get_error_message()

    assert "Username and password do not match any user in this service" in error_message


    #empty username
def test_empty_username(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_password("secret_sauce")
    login_page.click_login()

    error_message = login_page.get_error_message()

    assert "Username is required" in error_message


    #empty password
def test_empty_password(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.click_login()

    error_message = login_page.get_error_message()

    assert "Password is required" in error_message   

    #both empty field username and password
def test_both_fields_empty(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.click_login()

    error_message = login_page.get_error_message()

    assert "Username is required" in error_message