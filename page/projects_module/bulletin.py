from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


class Bulletin():

    bulletin_textbox = "au.geekseat.com.hub3candroid:id/edit_input_bulletin"
    bulletin_post_button = "au.geekseat.com.hub3candroid:id/btn_save_bulletin"
    bulletin_poster = "au.geekseat.com.hub3candroid:id/tv_user_name"
    bulletin_poster_picture = "au.geekseat.com.hub3candroid:id/riv_thumbnail"
    bulletin_content = "au.geekseat.com.hub3candroid:id/tv_text"
    bulletin_time = "au.geekseat.com.hub3candroid:id/tv_time"
    bulletin_like_button = "au.geekseat.com.hub3candroid:id/iv_like"
    bulletin_like_total = "au.geekseat.com.hub3candroid:id/tv_like"
    bulletin_comment_button = "au.geekseat.com.hub3candroid:id/iv_comment"
    bulletin_comment_total = "au.geekseat.com.hub3candroid:id/tv_comment"
    load_more_button = "au.geekseat.com.hub3candroid:id/btn_view_all"