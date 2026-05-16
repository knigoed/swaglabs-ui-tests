from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.wrong_username_or_password_alert = page.locator('[data-test="error"]')

    def fill_login_form(self, user_name: str, password: str):
        self.username_input.fill(user_name)
        expect(self.username_input).to_have_value(user_name)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_login_button(self):
        self.login_button.click()

    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_username_or_password_alert ).to_be_visible()
        expect(self.wrong_username_or_password_alert ).to_have_text(
            'Epic sadface: Username and password do not match any user in this service')
