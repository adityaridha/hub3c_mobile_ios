from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
from util import utility
import pytest
import time
import datetime
import pytz

raw_date= str(datetime.datetime.now(pytz.timezone('Asia/Jakarta')))
date = raw_date[0:-13]

class EditProject():

    el_project_name_id = "au.geekseat.com.hub3candroid:id/edit_project_name"
    el_project_code_id = "au.geekseat.com.hub3candroid:id/edit_project_code"
    el_project_description_id = "au.geekseat.com.hub3candroid:id/edit_description"
    el_currency_id = "au.geekseat.com.hub3candroid:id/spinner_currency"
    el_project_status_id = "au.geekseat.com.hub3candroid:id/spinner_status"
    el_proposed_start_id = "au.geekseat.com.hub3candroid:id/edit_proposed_start"
    el_proposed_end_id = "au.geekseat.com.hub3candroid:id/edit_proposed_end"
    el_actual_start_id = "au.geekseat.com.hub3candroid:id/edit_actual_start"
    el_date_completed_id = "au.geekseat.com.hub3candroid:id/edit_date_complete"
    el_reminder_date_id = "au.geekseat.com.hub3candroid:id/edit_reminder_date"
    el_billing_type_id = "au.geekseat.com.hub3candroid:id/spinner_billing_type"
    el_fixed_price_amount_id = "au.geekseat.com.hub3candroid:id/edit_fixed_amount"
    el_save_buton_id = "au.geekseat.com.hub3candroid:id/btn_add"
    el_cancel_button_id = "au.geekseat.com.hub3candroid:id/btn_add"

    def __init__(self, driver):
        self.driver = driver
        self.util = utility.Helper(driver=self.driver)

    def edit_project_name(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.el_project_name_id)))
        except TimeoutException:
            print("Edit project not ready")

        project_name = self.driver.find_element_by_id(self.el_project_name_id)
        project_name.clear()
        project_name.send_keys("Project edited {}".format(time.time()))

    def edit_project_code(self):
        project_code = self.driver.find_element_by_id(self.el_project_code_id)
        project_code.clear()
        project_code.send_keys("Code edited")

    def edit_project_description(self):
        description = self.driver.find_element_by_id(self.el_project_description_id)
        description.clear()
        description.send_keys("Description edited")

    def edit_currency(self):
        currency_el = self.driver.find_element_by_id(self.el_currency_id)
        print(currency_el.text)
        self.util.tap_spinner_options(spinner=currency_el, index=2)
        print("Edit currency")

    def edit_project_status(self):
        status_el = self.driver.find_element_by_id(self.el_project_status_id)
        self.util.tap_spinner_options(spinner=status_el, index=3)

    def edit_proposed_start(self):
        self.driver.find_element_by_id(self.el_proposed_start_id).click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='2018']").click() #harus diganti locator nya

        #//*[@contentDescription='2018']
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def edit_proposed_end(self):
        self.driver.find_element_by_id(self.el_proposed_end_id).click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='2018']").click() #harus diganti locator nya

        #//*[@contentDescription='2018']
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def edit_actual_start(self):
        self.driver.find_element_by_id(self.el_actual_start_id).click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='2018']").click() #harus diganti locator nya

        #//*[@contentDescription='2018']
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def edit_date_completed(self):
        pass

    def edit_reminder_date(self):
        self.driver.find_element_by_id(self.el_reminder_date_id).click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='2018']").click() #harus diganti locator nya

        #//*[@contentDescription='2018']
        self.driver.find_element_by_id("au.geekseat.com.hub3candroid:id/ok").click()

    def edit_billing_type(self):
        pass

    def edit_fixed_price_amount(self):
        fixed_price = self.driver.find_element_by_id(self.el_fixed_price_amount_id)
        fixed_price.clear()
        fixed_price.send_keys("999")

    def save_edit_project(self):
        self.driver.find_element_by_id(self.el_save_buton_id).click()

    def tap_cancel_button(self):
        self.driver.find_element_by_id(self.el_cancel_button_id).click()




