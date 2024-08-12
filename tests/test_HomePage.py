import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info('First name is '+getData['firstname'])
        homePage.getName().send_keys(getData['firstname'])
        homePage.getEmail().send_keys(getData['email'])
        homePage.getPassword().send_keys(getData['password'])
        homePage.getCheckbox().click()
        homePage.getCheckbox().click()
        self.selectOptionByText(homePage.getGender(), getData['gender'])

        homePage.submitForm().click()
        alert = homePage.getAlert().text

        assert 'Success' in alert
        self.driver.refresh()

    @pytest.fixture(params= HomePageData.getTestData("testCase2"))
    def getData(self, request):
        return request.param
