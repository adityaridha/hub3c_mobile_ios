from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


class Agenda():

    agenda_daytitle = "au.geekseat.com.hub3candroid:id/textToday"
    agenda_prevday_button = "au.geekseat.com.hub3candroid:id/imagePrev"
    agenda_nextday_button = "au.geekseat.com.hub3candroid:id/imagePrev"
    agenda_daterange = "au.geekseat.com.hub3candroid:id/textDateRange"
    agenda_date = "au.geekseat.com.hub3candroid:id/textDayNumber"
    agenda_month = "au.geekseat.com.hub3candroid:id/textMonthName"
    agenda_time = "au.geekseat.com.hub3candroid:id/textDuration"
    agenda_day = "au.geekseat.com.hub3candroid:id/textDayName"
    agenda_title = "au.geekseat.com.hub3candroid:id/textTitle"
    agenda_description = "au.geekseat.com.hub3candroid:id/textDescription"
    agenda_more_button = "au.geekseat.com.hub3candroid:id/ib_action_more"
    load_more_button= "au.geekseat.com.hub3candroid:id/btn_view_all"

    ''' option more button '''
    more_agenda_title = "au.geekseat.com.hub3candroid:id/text_tittle"
    agenda_edit_button = "au.geekseat.com.hub3candroid:id/btn_edit"
    agenda_delete_button = "au.geekseat.com.hub3candroid:id/btn_delete"