from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.TAG_NAME, "h4")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkoutPageBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def getCardTitles(self):
        return  self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getCheckoutPageBtn(self):
        return self.driver.find_element(*CheckoutPage.checkoutPageBtn)

    def getCheckoutBtn(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage


