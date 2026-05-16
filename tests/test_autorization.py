from playwright.sync_api import expect, Page
import pytest

class TestRegistration:
    def test_success_login(self, chromium_page: Page) -> None:
        chromium_page.goto('https://www.saucedemo.com/')

        chromium_page.locator('[data-test="username"]').fill('standard_user')
        chromium_page.locator('[data-test="password"]').fill('secret_sauce')

        chromium_page.locator('[data-test="login-button"]').click()

        expect(
            chromium_page.locator('[data-test="primary-header"]')
            ).to_be_visible()

        chromium_page.wait_for_timeout(5000)



    @pytest.mark.parametrize('username, password', [("user", "secret_sauce"),
                                                 ("standard_user", "password"),
                                                 ("user", "password")])
    def test_wrong_username_or_password_registration(self, chromium_page: Page, username: str, password: str):
        chromium_page.goto('https://www.saucedemo.com/')

        chromium_page.locator('[data-test="username"]').fill(username)
        chromium_page.locator('[data-test="password"]').fill(password)

        chromium_page.locator('[data-test="login-button"]').click()

        wrong_username_or_password_alert = chromium_page.locator('[data-test="error"]')

        expect(wrong_username_or_password_alert).to_be_visible()
        expect(wrong_username_or_password_alert).to_have_text(
            'Epic sadface: Username and password do not match any user in this service')

        chromium_page.wait_for_timeout(5000)


