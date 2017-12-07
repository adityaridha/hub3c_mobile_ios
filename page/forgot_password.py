from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest


class ForgotPassword():


    email = "au.geekseat.com.hub3candroid:id/editEmail"
    reset_btn = "au.geekseat.com.hub3candroid:id/buttonReset"


    def __init__(self, driver):
        self.driver = driver

    def input_email(self):
        self.driver.find_element_by_id(self.email).send_keys("tony.stark@mailinator.com")
    #
    # def tap_get_reset_link(self):
    #
