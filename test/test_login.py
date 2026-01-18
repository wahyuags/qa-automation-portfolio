from pages.login_page import LoginPage
from config.config import (
    BASE_URL,
    VALID_USER,
    VALID_PASS,
    INVALID_USER,
    INVALID_PASS
)
from utils.screenshot import take_screenshot


def test_login_invalid(driver):
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.login(INVALID_USER, INVALID_PASS)

    take_screenshot(driver, "invalid_login")

    assert "Your username is invalid" in login.get_flash_text()


def test_login_valid(driver):
    """
    User can login with valid credentials
    """
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.login(VALID_USER, VALID_PASS)

    assert "You logged into a secure area!" in login.get_flash_text()


def test_logout(driver):
    """
    User can logout successfully
    """
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.login(VALID_USER, VALID_PASS)
    login.logout()

    assert "You logged out of the secure area!" in login.get_flash_text()


