import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info('Getting all the cards text')
        #checkoutPage = CheckoutPage(self.driver)
        cards = checkoutPage.getCardTitles()


        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if "Blackberry" in cardText:
                checkoutPage.getCardFooter()[i].click()

        checkoutPage.getCheckoutPageBtn().click()
        #checkoutPage.getCheckoutBtn().click()

        #confirmPage = ConfirmPage(self.driver)
        confirmPage = checkoutPage.getCheckoutBtn()
        log.info('Entering country name')
        confirmPage.getCountryField().send_keys('ind')

        self.verifyLinkPresence('India')

        confirmPage.getCountry().click()
        confirmPage.getCheckbox().click()
        confirmPage.getSubmitBtn().click()
        msg = confirmPage.getAlertMsg().text
        log.info('Text received form application: '+msg)
        assert 'Success' in msg
