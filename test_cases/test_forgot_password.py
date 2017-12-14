import sys
import os
import pytest
import time
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
import page
from util import utility
from connection import Connection

directory = '%s/' % os.getcwd()

driver = Connection.driver
login = page.Login(driver)
util = utility.Helper(driver)
forgot_pass = page.ForgotPassword(driver)

class TestForgotPass():

    def test_forgot_password_valid_email(self):
        driver.launch_app()
        login.verify_all_element()
        login.tap_forgot_password()
        forgot_pass.input_email(email="fakerandomemail@mailinator.com")
        forgot_pass.tap_get_reset_link()
        forgot_pass.verify_email_unregistered()

    def test_forgot_password_invalid_format(self):
        driver.launch_app()
        login.verify_all_element()
        login.tap_forgot_password()
        forgot_pass.input_email(email="tonystark@gmail")
        forgot_pass.tap_get_reset_link()
        forgot_pass.verify_email_unregistered()

