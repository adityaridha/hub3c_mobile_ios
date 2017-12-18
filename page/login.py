from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

import time
import pytest



class Login():

    username_xpath = '//XCUIElementTypeApplication[@name="Hub3c"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField'
    password_xpath = '//XCUIElementTypeApplication[@name="Hub3c"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField'
    el_sign_in_button_id = 'Sign In'
    el_reister_id = "Create Account"
    el_icon_id = "hub3cLogo"
    el_alert_id = "SCLAlertView"
    el_warning_button_id = "Done"
    el_forgot_pass_id = "Forgot Password"
    el_BACK_id = "Back"


    def __init__(self, driver):
        self.driver = driver

    def verify_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH, self.username_xpath)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.password_xpath)))
            self.driver.find_element_by_id(self.el_icon_id).click()
            print("\nlogin element is ready")
        except TimeoutException:
            print("login element not ready")


    def handle_error_simulator(self):
        self.driver.hide_keyboard()
        self.driver.find_element_by_id(self.el_icon_id).click() ### necessary for compeletely hide keyboard
        self.driver.find_element_by_id(self.el_reister_id).click()
        try:
            WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((By.ID, self.el_BACK_id)))
        except TimeoutException:
            print("No back button to login screen")

        self.driver.find_element_by_id(self.el_BACK_id).click()

    def verify_login_alert(self):
        try:
            WebDriverWait(self.driver, 15).until(ec.presence_of_element_located((By.ID, self.el_alert_id)))
            print("Login Failed as intended")
        except TimeoutException:
            print("Something when wrong, there should be a warning")

    def login(self, email, password):
        self.driver.launch_app()
        self.handle_error_simulator()
        self.input_email(email=email)
        self.input_password(password=password)
        self.driver.find_element_by_id(self.el_sign_in_button_id).click()

    def input_email(self, email):
        self.verify_all_element()
        self.handle_error_simulator()
        email_el = self.driver.find_element_by_xpath(self.username_xpath)
        email_el.clear()
        # self.driver.set_value(email_el, email)
        email_el.send_keys(email)
        self.driver.hide_keyboard()

    def input_password(self, password):
        password_el = self.driver.find_element_by_xpath(self.password_xpath)
        password_el.clear()
        # self.driver.set_value(password_el, password)
        password_el.send_keys(password)
        self.driver.hide_keyboard()

    def tap_sign_in(self):
        self.driver.find_element_by_id(self.el_sign_in_button_id).click()

    def is_login_success(self):
        pass

    def tap_registration(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.el_reister_id)))
        except TimeoutException:
            print("Create account button not found")

        regis_el = self.driver.find_element_by_id(self.el_reister_id)
        regis_el.click()


    def tap_forgot_password(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.el_forgot_pass_id)))
        except TimeoutException:
            print("Forgot password not found")

        self.driver.find_element_by_id(self.el_forgot_pass_id).click()


    def close_warning(self):
        self.driver.find_element_by_id(self.el_warning_button_id).click()