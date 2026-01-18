from selenium.webdriver.common.by import By

class SecurePage:
    def __init__(self, driver):
        self.driver = driver

    flash_message = (By.ID, "flash")
    logout_button = (By.CSS_SELECTOR, "a.button")

    def get_message(self):
        return self.driver.find_element(*self.flash_message).text

    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()
