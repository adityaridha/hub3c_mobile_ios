from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import time


class Navbar():


    dashboard_xpath = "//XCUIElementTypeApplication[@name='Hub3c']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeButton[1]"
    comp_prof_xpath = "//XCUIElementTypeApplication[@name='Hub3c']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeButton[2]"
    team_member_id = "Team Member"
    network_xpath = "//XCUIElementTypeButton[@name='Network']"
    features_id = "Menu"

    def __init__(self, driver):
        self.driver = driver

    def tap_dashboard(self):
        pass

    def tap_team_members(self):
        pass

    def tap_business_connections(self):
        pass

    def tap_feature_menu(self):

        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.features_id)))
            print("Features menu is Ready")
        except TimeoutException:
            print("Can't tap feature menu")

        self.driver.find_element_by_id(self.features_id).click()