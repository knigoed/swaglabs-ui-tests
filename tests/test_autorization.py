import pytest
from playwright.sync_api import expect, Page
from pages.authentication.login_page import LoginPage

class TestRegistration:
    def test_success_login(self, chromium_page: Page) -> None:
        login_page = LoginPage(page=chromium_page)

        login_page.visit('https://www.saucedemo.com/')

        login_page.fill_login_form(user_name='standard_user', password='secret_sauce')

        login_page.login_button.click()

        expect(
            chromium_page.locator('[data-test="primary-header"]')
            ).to_be_visible()

        chromium_page.wait_for_timeout(5000)



    @pytest.mark.parametrize('username, password', [("user", "secret_sauce"),
                                                 ("standard_user", "password"),
                                                 ("user", "password")])
    def test_wrong_username_or_password_registration(self, chromium_page: Page, username: str, password: str):
        login_page = LoginPage(page=chromium_page)

        login_page.visit('https://www.saucedemo.com/')

        login_page.fill_login_form(user_name=username, password=password)

        login_page.login_button.click()

        login_page.check_visible_wrong_email_or_password_alert()

        chromium_page.wait_for_timeout(5000)


