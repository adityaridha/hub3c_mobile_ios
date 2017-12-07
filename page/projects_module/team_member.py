from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import datetime
import pytz
import time


class TeamMember():

    team_member_total = "au.geekseat.com.hub3candroid:id/tv_sum_team"
    team_member_name = "au.geekseat.com.hub3candroid:id/tv_name"
    team_member_picture = "(//*[@id='rv_team_project']/*/*/*/*[@class='android.widget.ImageView' and @width>0 and ./parent::*[./parent::*[@id='layout_main']]])[1]"
    team_member_role = "au.geekseat.com.hub3candroid:id/tv_job"
    team_member_status = "au.geekseat.com.hub3candroid:id/iv_online_status"
    team_member_more_button = "au.geekseat.com.hub3candroid:id/ib_action_more"
    add_team_member = "au.geekseat.com.hub3candroid:id/fab"
    load_more_button = "au.geekseat.com.hub3candroid:id/btn_view_all"

    ''' option more button '''
    more_team_member_name = "au.geekseat.com.hub3candroid:id/text_tittle"
    more_team_member_edit = "au.geekseat.com.hub3candroid:id/btn_edit"
    more_team_member_delete = "au.geekseat.com.hub3candroid:id/btn_delete"