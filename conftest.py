import sys
import os
import pytest
from pathlib import Path
root = Path(__file__).parents[0]   #get the root directory
root_model = str(root)
sys.path.append(root_model)
print(root_model)
print(sys.path)
import page
from connection import Connection
from util import utility
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = Connection.driver
login = page.Login(driver)
dashboard = page.Dashboard(driver)
navbar = page.Navbar(driver)
feature_menu = page.Feature(driver)
user_profile = page.UserProfile(driver)
util = utility.Helper(driver)


@pytest.fixture()
def reset_app_android():
    os.system("adb shell pm clear au.geekseat.com.hub3candroid")

@pytest.fixture()
def relogin():
    try :
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, dashboard.invite_member)))
        is_dashboard = True
    except TimeoutException:
        is_dashboard = False

    print("\nis Dashboard : {}".format(is_dashboard))

    if is_dashboard == True :
        navbar.tap_feature_menu()
        feature_menu.tap_header(user_name="John Doe")
        util.swipe_to_bottom(target_element=user_profile.loc_logout_id)
        user_profile.tap_logout()

    else:
        print("Start with new session")


@pytest.mark.hookwrapper
def pytest_runtest_makereport():

    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            driver.get_screenshot_as_file(file_name)


