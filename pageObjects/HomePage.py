from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, 'email')
    password = (By.ID, 'exampleInputPassword1')
    checkbox = (By.ID, 'exampleCheck1')
    radioBtn = (By.CSS_SELECTOR, '#inlineRadio1')
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, 'alert-success')
    def shopItems(self):
       self.driver.find_element(*HomePage.shop).click()
       checkoutPage = CheckoutPage(self.driver)
       return  checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getRadioBtn(self):
        return self.driver.find_element(*HomePage.radioBtn)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)
