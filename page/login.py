from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest



class Login():

    username_id = 'au.geekseat.com.hub3candroid:id/textUsername'
    password_id = 'au.geekseat.com.hub3candroid:id/textPassword'
    sign_in_button = 'au.geekseat.com.hub3candroid:id/buttonLogin'
    register_forgot_password = "au.geekseat.com.hub3candroid:id/textForgotPassword"


    def __init__(self, driver):
        self.driver = driver

    def verified_all_element(self):
        try:
            self.driver.find_element_by_id(self.username_id)
            self.driver.find_element_by_id(self.password_id)
        except NoSuchElementException:
            pytest.fail("Element fail")

    def login(self, email, password):
        self.driver.launch_app()
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.username_id)))
        except TimeoutException:
            print("element not ready")

        self.driver.find_element_by_id(self.username_id).send_keys(email)
        self.driver.find_element_by_id(self.password_id).send_keys(password)
        self.driver.find_element_by_id(self.sign_in_button).click()

    def input_email(self, email):
        try:
            WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.ID, self.username_id)))
        except TimeoutException:
            print("element not ready")
        email_el = self.driver.find_element_by_id(self.username_id)
        email_el.send_keys(email)

    def input_password(self, password):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.register_forgot_password)))
        except TimeoutException:
            print("element not ready")
        password_el = self.driver.find_element_by_id(self.password_id)
        password_el.send_keys(password)

    def tap_sign_in(self):
        self.driver.find_element_by_id(self.sign_in_button).click()

    def is_login_success(self):
        pass

    def tap_registration(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.register_forgot_password)))
        except TimeoutException:
            print("element not ready")

        register =  self.driver.find_element_by_id(self.register_forgot_password)
        x = register.location['x']
        y = register.location['y']
        positions = []
        positions.append((x + 10, y))
        positions.append((x + 20, y))
        self.driver.tap(positions)

    def tap_forgot_password(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.username_id)))
        except TimeoutException:
            print("element not ready")

        forgot_pass =  self.driver.find_element_by_id('au.geekseat.com.hub3candroid:id/textForgotPassword')
        x = forgot_pass.location['x']
        y = forgot_pass.location['y']
        # height = forgot_pass.size['height']
        width = forgot_pass.size['width']

        positions = []
        positions.append((x + width - 20, y))
        positions.append((x + width - 10, y))
        print(positions)
        self.driver.tap(positions)