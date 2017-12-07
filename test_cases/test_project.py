import sys
import pytest
import time
from pathlib import Path
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
import page
from connection import Connection
from util import utility

driver = Connection.driver

login = page.Login(driver)
dashboard = page.Dashboard(driver)
navbar = page.Navbar(driver)
feature_menu = page.Feature(driver)
project = page.ProjectList(driver)
create_project = page.CreateNewProject(driver)
edit_project = page.EditProject(driver)
util = utility.Helper(driver)

@pytest.mark.usefixtures("reset_app")
class TestProject():

    def test_create_project_minimum_req(self):
        login.login(email="transsystem@mailinator.com", password="ZXasqw12")
        dashboard.verified_all_element()
        navbar.tap_feature_menu()
        feature_menu.tap_projects()
        project.tap_create_new_project()
        create_project.verified_form()
        create_project.input_project_title()
        create_project.tap_next()
        create_project.tap_next()
        create_project.handle_team_member_validation()
        create_project.tap_complete()
        create_project.handle_activity_validation()

    def test_create_project_with_unidentified_team_member(self):
        login.login(email="transsystem@mailinator.com", password="ZXasqw12")
        dashboard.verified_all_element()
        navbar.tap_feature_menu()
        feature_menu.tap_projects()
        project.tap_create_new_project()

        ### ############### input basic information
        create_project.verified_form()
        create_project.input_project_title()
        create_project.input_project_code()
        create_project.input_project_desc()
        util.swipe_to_buttom()
        create_project.set_reminder_date()
        util.swipe_to_buttom()
        create_project.tap_next()

        ### ############### Add team member project
        create_project.input_team_member_name(teamm_ember_name="Aditya Ridha")
        create_project.set_project_role()
        create_project.set_hourly_rate()
        util.swipe_to_buttom()
        create_project.tap_add_member_button()
        create_project.tap_option_team_member()
        create_project.tap_popup_edit()
        create_project.set_hourly_rate()
        util.swipe_to_buttom()
        create_project.tap_add_member_button()
        create_project.tap_next()

        ### ############### Add project activity
        create_project.tap_complete()
        create_project.handle_activity_validation()

    # @pytest.mark.skip
    def test_create_project_all_form_filled(self):
        login.login(email="transsystem@mailinator.com", password="ZXasqw12")
        dashboard.verified_all_element()
        navbar.tap_feature_menu()
        feature_menu.tap_projects()
        project.tap_create_new_project()

        ### ############### input basic information
        create_project.verified_form()
        create_project.input_project_title()
        create_project.input_project_code()
        create_project.input_project_desc()
        util.swipe_to_buttom()
        create_project.set_reminder_date()
        util.swipe_to_buttom()
        create_project.tap_next()

        ### ############### Add team member project
        create_project.input_team_member_name(teamm_ember_name="Jovan")
        create_project.set_project_role()
        create_project.set_hourly_rate()
        util.swipe_to_buttom()
        create_project.tap_add_member_button()
        create_project.tap_option_team_member()
        create_project.tap_popup_edit()
        create_project.set_hourly_rate()
        util.swipe_to_buttom()
        create_project.tap_add_member_button()
        create_project.tap_next()

        ### ############### Add project activity
        create_project.input_activity_subject()
        create_project.input_activity_description()
        create_project.select_activity_type()
        util.swipe_to_buttom()
        create_project.set_schedule_start()
        util.swipe_to_buttom()
        create_project.set_is_billible()
        util.swipe_to_buttom()
        create_project.tap_save_activity()
        create_project.tap_complete()

    def test_create_project_with_two_project_owner(self):
        login.login(email="transsystem@mailinator.com", password="ZXasqw12")
        dashboard.verified_all_element()
        navbar.tap_feature_menu()
        feature_menu.tap_projects()
        project.tap_create_new_project()

        ### ############### input basic information
        create_project.verified_form()
        create_project.input_project_title()
        create_project.input_project_code()
        create_project.input_project_desc()
        util.swipe_to_buttom()
        create_project.set_reminder_date()
        util.swipe_to_buttom()
        create_project.tap_next()

        ### ############### Add team member project
        create_project.input_team_member_name(teamm_ember_name="Jovan")
        create_project.set_project_role()
        create_project.set_hourly_rate()
        util.swipe_to_buttom()
        create_project.set_is_project_owner()
        create_project.tap_add_member_button()
        create_project.tap_option_team_member()
        create_project.tap_popup_edit()
        create_project.set_hourly_rate()
        util.swipe_to_buttom()
        create_project.tap_add_member_button()
        create_project.tap_next()

        ### ############### Add project activity
        create_project.input_activity_subject()
        create_project.input_activity_description()
        create_project.select_activity_type()
        util.swipe_to_buttom()
        create_project.set_schedule_start()
        util.swipe_to_buttom()
        create_project.set_is_billible()
        util.swipe_to_buttom()
        create_project.tap_save_activity()
        create_project.tap_complete()


    def test_edit_project(self):
        login.login(email="transsystem@mailinator.com", password="ZXasqw12")
        dashboard.verified_all_element()
        navbar.tap_feature_menu()
        feature_menu.tap_projects()
        project.tap_option_for_project()
        project.tap_edit_button()
        edit_project.edit_project_name()
        edit_project.edit_project_code()
        edit_project.edit_project_description()
        edit_project.edit_currency()
        edit_project.edit_project_status()
        edit_project.edit_proposed_end()
        util.swipe_to_buttom()
        # edit_project.edit_fixed_price_amount()
        edit_project.save_edit_project()


    def test_delete_project(self):
        login.login(email="transsystem@mailinator.com", password="ZXasqw12")
        dashboard.verified_all_element()
        navbar.tap_feature_menu()
        feature_menu.tap_projects()
        project.tap_option_for_project()
        project.tap_delete_button()
        project.proceed_delete_action()
        project.verified_delete_project()

    def test_search_project(self):
        pass

    def test_arcived_project(self):
        pass

    def test_start_project(self):
        pass





