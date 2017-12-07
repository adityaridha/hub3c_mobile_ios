from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


class Notes():

    notes_textbox = "au.geekseat.com.hub3candroid:id/edit_input_note"
    notes_save_button = "au.geekseat.com.hub3candroid:id/btn_save_note"
    search_textfield = "android:id/search_src_text"
    notes_poster = "au.geekseat.com.hub3candroid:id/tv_name"
    notes_poster_picture = "(//*[@id='rv_notes_project']/*/*/*[@class='android.widget.ImageView' and @width>0 and @height>0 and ./following-sibling::*[./*[@id='tv_name']]])[1]"
    notes_time = "au.geekseat.com.hub3candroid:id/tv_time"
    notes_title = "au.geekseat.com.hub3candroid:id/tv_subject_note"
    notes_content = "au.geekseat.com.hub3candroid:id/tv_note"
    notes_edit_button = "au.geekseat.com.hub3candroid:id/btn_edit"
    load_more_button = "au.geekseat.com.hub3candroid:id/btn_view_all"

    ''' edit notes '''

    edit_notes_textbox = "au.geekseat.com.hub3candroid:id/et_file_name"
    edit_notes_cancel = "//*[@id='button2']"
    edit_notes_save= "//*[@id='button1']"