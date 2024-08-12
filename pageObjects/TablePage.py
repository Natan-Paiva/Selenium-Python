from selenium.webdriver.common.by import By


class TablePage():
    def __init__(self, driver):
        self.driver = driver

    download = (By.CSS_SELECTOR, '#downloadButton')
    upload = (By.CSS_SELECTOR, "input[type='file']")

    def getDownloadBtn(self):
        return self.driver.find_element(*TablePage.download)

    def getUploadBtn(self):
        return self.driver.find_element(*TablePage.upload)
