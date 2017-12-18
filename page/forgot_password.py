from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest


class ForgotPassword():


    loc_email_xpath = '//XCUIElementTypeApplication[@name="Hub3c"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField'
    loc_reset_btn_id = "Get Reset Link"
    loc_message_warning_xpath = '//XCUIElementTypeOther[@name="SCLAlertView"]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextView'
    value_success = 'Your reset email is processed please check your e-mail'
    value_unregistered = 'The Email you entered does not exist. Please try again.'
    value_invalid = 'Invalid email'
    loc_done_button_id = 'Done'
    loc_success_alert_id = 'Success'
    loc_invalid_id = 'Message Info'
    loc_warning_id = 'Warning'


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
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.loc_warning_id)))
            warning = self.driver.find_element_by_xpath(self.loc_message_warning_xpath).get_attribute(name="value")
            print("\n" + warning)
            if warning != self.value_unregistered:
                pytest.fail()
            print("Email is unregistered as expected")
        except TimeoutException:
            print("Warning not found")

    def verify_email_is_sent(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.loc_success_alert_id)))
            warning = self.driver.find_element_by_xpath(self.loc_message_warning_xpath).get_attribute(name="value")
            print("\n" + warning)
            if warning != self.value_success:
                pytest.fail()
        except TimeoutException:
            print("Warning not found")

        self.driver.find_element_by_id(self.loc_done_button_id).click()

    def verify_invalid_format(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.loc_invalid_id)))
            warning = self.driver.find_element_by_xpath(self.loc_message_warning_xpath).get_attribute(name="value")
            print("\n" + warning)
            if self.value_invalid not in warning:
                pytest.fail()
        except TimeoutException:
            print("Warning not found")






