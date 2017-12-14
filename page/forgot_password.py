from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest


class ForgotPassword():


    loc_email_xpath = '//XCUIElementTypeApplication[@name="Hub3c"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField'
    loc_reset_btn_id = "Get Reset Link"
    warning_xpath = '//XCUIElementTypeOther[@name="SCLAlertView"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextView'
    unregis_email_allert = 'The Email you entered does not exist. Please try again.'


    def __init__(self, driver):
        self.driver = driver

    def input_email(self, email):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.loc_email_xpath)))
        except TimeoutException:
            pytest.fail()
            print("Email text box not found")
        self.driver.find_element_by_xpath(self.loc_email_xpath).send_keys(email)

    def tap_get_reset_link(self):
        self.driver.find_element_by_id(self.loc_reset_btn_id).click()

    def verify_email_unregistered(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.warning_xpath)))
            warning = self.driver.find_element_by_xpath(self.warning_xpath).get_attribute(name="value")
            print(warning)
            if warning != self.unregis_email_allert:
                pytest.fail()
            print("Email is unregistered as expected")
        except TimeoutException:
            print("Warning not found")

