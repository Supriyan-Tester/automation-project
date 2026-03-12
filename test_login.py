import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto("https://www.saucedemo.com")
        yield page
        browser.close()

def test_login(page):
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        assert page.url == "https://www.saucedemo.com/inventory.html"
        print("Login Test Passed")
        
def test_failed_login(page):
        page.locator("#user-name").fill("Wrong Username")
        page.locator("#password").fill("wrong password")
        page.locator("#login-button").click()
        error_message = page.locator("[data-test='error']").inner_text()
        assert "Epic sadface" in error_message
        print ("Failed Login Test Passed")
        