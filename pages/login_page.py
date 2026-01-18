from selenium.webdriver.common.by import By
from core.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button.radius")
    FLASH_MSG = (By.ID, "flash")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def open(self, url):
        self.driver.get(url)

    def login(self, user, password):
        self.type(self.USERNAME, user)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_flash_displayed(self):
        return self.wait_visible(self.FLASH_MSG).is_displayed()

    def get_flash_text(self):
        return self.wait_visible(self.FLASH_MSG).text

    def logout(self):
        self.click(self.LOGOUT_BTN)
