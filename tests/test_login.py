import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import allure

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

@allure.feature("Login")
def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_products_page()
    assert "inventory" in page.url

@allure.feature("Login")
def test_invalid_password(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "wrong_password")
    assert "username and password do not match" in login_page.get_error_message().lower()

@allure.feature("Login")
def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    assert "locked out" in login_page.get_error_message().lower()

@allure.feature("Login")
def test_empty_fields(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("", "")
    assert "username is required" in login_page.get_error_message().lower()

@allure.feature("Login")
def test_performance_glitch_user(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("performance_glitch_user", "secret_sauce")
    assert login_page.is_products_page()
    assert "inventory" in page.url
    