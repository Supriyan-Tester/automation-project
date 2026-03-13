
from pages.login_page import LoginPage

def test_login(page):
    login = LoginPage(page)
    login.login("standard_user" , "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"
    print("Login test passed")

def test_failed_login(page):
    login = LoginPage(page)
    login.login("Wrong_User" , "Wrong_Password")
    error_message = page.locator("[data-test='error']").inner_text()
    assert "Epic sadface" in error_message
    print("Failed login test passed!")