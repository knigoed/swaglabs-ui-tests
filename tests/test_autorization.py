from playwright.sync_api import sync_playwright, expect
import pytest

class TestRegistration:
    def test_success_login(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto('https://www.saucedemo.com/')

            page.locator('[data-test="username"]').fill('standard_user')
            page.locator('[data-test="password"]').fill('secret_sauce')

            page.locator('[data-test="login-button"]').click()

            expect(
                page.locator('[data-test="primary-header"]')
            ).to_be_visible()

            page.wait_for_timeout(5000)

            browser.close()

    @pytest.mark.parametrize('username, password', [("user", "secret_sauce"),
                                                 ("standard_user", "password"),
                                                 ("user", "password")])
    def test_wrong_username_or_password_registration(self, username: str, password: str):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto('https://www.saucedemo.com/')

            page.locator('[data-test="username"]').fill(username)
            page.locator('[data-test="password"]').fill(password)

            page.locator('[data-test="login-button"]').click()

            wrong_username_or_password_alert = page.locator('[data-test="error"]')

            expect(wrong_username_or_password_alert).to_be_visible()
            expect(wrong_username_or_password_alert).to_have_text(
                'Epic sadface: Username and password do not match any user in this service')

            page.wait_for_timeout(5000)

            browser.close()
