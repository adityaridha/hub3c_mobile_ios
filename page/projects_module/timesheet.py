from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


class Timesheet():

    timesheet_title = "au.geekseat.com.hub3candroid:id/tv_tittle"
    timesheet_progress_bar = "au.geekseat.com.hub3candroid:id/materialProgress"
    timesheet_progress = "au.geekseat.com.hub3candroid:id/tv_text_progress"
    timesheet_hours_spent = "au.geekseat.com.hub3candroid:id/tv_hour_spent"
    timesheet_budget_hours = "au.geekseat.com.hub3candroid:id/tv_complete_progress"