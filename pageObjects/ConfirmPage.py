from selenium.webdriver.common.by import By
class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    countrySel = (By.CSS_SELECTOR, '#country')
    country = (By.LINK_TEXT, 'India')
    checkbox = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    msg = (By.CLASS_NAME, 'alert-success')

    def getCountryField(self):
        return self.driver.find_element(*ConfirmPage.countrySel)
    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)
    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
    def getSubmitBtn(self):
        return self.driver.find_element(*ConfirmPage.submit)
    def getAlertMsg(self):
        return self.driver.find_element(*ConfirmPage.msg)

