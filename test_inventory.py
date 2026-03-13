from pages.login_page import LoginPage

def test_inventory_page_loads(page):
    login = LoginPage(page)
    login.login("standard_user","secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"
    print("Page Loads Successfully")