from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


class Attachment():

    attachment_name = "au.geekseat.com.hub3candroid:id/tv_name_file"
    attachment_picture = "au.geekseat.com.hub3candroid:id/riv_thumbnail"
    attachment_uploader = "au.geekseat.com.hub3candroid:id/tv_name"
    attachment_more_button = "au.geekseat.com.hub3candroid:id/ib_action_more"
    add_attachment_button = "au.geekseat.com.hub3candroid:id/fab"
    load_more_button = "au.geekseat.com.hub3candroid:id/btn_view_all"

    ''' option more button '''

    more_attachment_name = "au.geekseat.com.hub3candroid:id/text_tittle"
    attachment_download = "au.geekseat.com.hub3candroid:id/btn_download"
    attachment_edit = "au.geekseat.com.hub3candroid:id/btn_edit"
    attachment_delete = "au.geekseat.com.hub3candroid:id/btn_delete"