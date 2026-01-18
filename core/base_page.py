from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait_visible(locator).click()

    def type(self, locator, text):
        el = self.wait_visible(locator)
        el.clear()
        el.send_keys(text)

