from playwright.sync_api import Page, expect

class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.page.fill("input#user-name", username)
        self.page.fill("input#password", password)
        self.page.click("input#login-button")

    def get_error_message(self) -> str:
        return self.page.locator("[data-test='error']").inner_text(timeout=5000)

    def is_products_page(self) -> bool:
        return self.page.locator(".title").is_visible(timeout=5000)
        