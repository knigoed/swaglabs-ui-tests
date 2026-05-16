from typing import Generator
import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture
def chromium_page() -> Generator[Page, None, None]:
   with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)

        yield browser.new_page()

        browser.close()