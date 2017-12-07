from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import time


class Navbar():


    dashboard = "au.geekseat.com.hub3candroid:id/tab_dashboard"
    business_profile = "au.geekseat.com.hub3candroid:id/tab_business"
    team_member = "au.geekseat.com.hub3candroid:id/tab_member"
    business_network = "au.geekseat.com.hub3candroid:id/tab_business_network"
    features = "au.geekseat.com.hub3candroid:id/tab_profile"

    def __init__(self, driver):
        self.driver = driver

    def tap_dashboard(self):
        pass

    def tap_team_members(self):
        pass

    def tap_business_connections(self):
        pass

    def tap_feature_menu(self):
        time.sleep(1)
        self.driver.find_element_by_id(self.features).click()