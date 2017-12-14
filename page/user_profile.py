from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest


class UserProfile():


    loc_logout_id = "Logout"
    switch_account = "au.geekseat.com.hub3candroid:id/buttonSwitch"
    edit = "au.geekseat.com.hub3candroid:id/action_edit"
    back = "//*[@contentDescription='Navigate up']"

    def __init__(self, driver):
        self.driver = driver

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.ID, self.loc_logout_id)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.switch_account)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.edit)))
            print("Dadshboard page is compleately loaded")
        except TimeoutException:
            print("element not ready")

    def tap_logout(self):

        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.loc_logout_id)))
            print("Log out button is found")
        except TimeoutException:
            print("Log out button not ready")


        self.driver.find_element_by_id(self.loc_logout_id).click()