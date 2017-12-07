from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium import webdriver
import pytest
import time


class ProjectList():

    create_project = "au.geekseat.com.hub3candroid:id/fab"  # generic floating button id
    project_on_top = "au.geekseat.com.hub3candroid:id/title"  # generic project id
    more_action = "au.geekseat.com.hub3candroid:id/ib_action_more"
    start_project = "au.geekseat.com.hub3candroid:id/textStartProject"
    activities_link = "au.geekseat.com.hub3candroid:id/counter"
    search_project = "au.geekseat.com.hub3candroid:id/action_search"
    back_to_dashboard = "//*[@contentDescription='Navigate up']"
    team_member_info = "(//*[@id='memberContainer']/*[@class='android.widget.ImageView' and @width>0])[1]"
    in_progress_list = "//*[@text='IN PROGRESS']"
    not_yet_started_list = "//*[@text='NOT YET STARTED']"
    on_hold_list = "//*[@text='ON HOLD']"
    cancelled_list = "//*[@text='CANCELLED']"
    completed_list = "//*[@text='COMPLETED']"
    archived_list = "//*[@text='ARCHIVED']"
    restore_button = "au.geekseat.com.hub3candroid:id/textDueDate"
    el_edit_project_id = "au.geekseat.com.hub3candroid:id/btn_edit"
    el_delete_project_id = "au.geekseat.com.hub3candroid:id/btn_delete"
    el_del_confirmation = "//*[@text='Deleting project will remove this project from list and turn off all notification. Do you want to continue?']"
    el_yes_button_for_delete_id = "android:id/button1"
    crouton_successfull_delete = "//*[@text='Project is successfully deleted']"

    def __init__(self, driver):
        self.driver = driver

    def tap_create_new_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.create_project)))
        except TimeoutException:
            print("Create project not ready")
        self.driver.find_element_by_id(self.create_project).click()

    def tap_option_for_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.more_action)))
        except TimeoutException:
            print("Project not ready")
        self.driver.find_element_by_id(self.more_action).click()

    def tap_edit_button(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.el_edit_project_id)))
        except TimeoutException:
            print("Create project not ready")
        self.driver.find_element_by_id(self.el_edit_project_id).click()

    def tap_delete_button(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.el_delete_project_id)))
        except TimeoutException:
            print("Create project not ready")
        self.driver.find_element_by_id(self.el_delete_project_id).click()

    def proceed_delete_action(self):
        try :
            WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.XPATH,self.el_del_confirmation)))
            self.driver.find_element_by_id(self.el_yes_button_for_delete_id).click()
        except TimeoutException:
            print("Delete confirmation not appear")
            pytest.fail()

    def verified_delete_project(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.crouton_successfull_delete)))
            print("Deletion success")
        except TimeoutException:
            print("Delete failed")
            pytest.fail()


