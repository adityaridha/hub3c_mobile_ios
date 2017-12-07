from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class Dashboard():


    notif = "au.geekseat.com.hub3candroid:id/notification_counter"
    connected = "au.geekseat.com.hub3candroid:id/textLinkConnected"
    pending = "au.geekseat.com.hub3candroid:id/textLinkPending"
    request = "au.geekseat.com.hub3candroid:id/textLinkRequests"
    invite_business = "au.geekseat.com.hub3candroid:id/textLinkInviteBusiness"
    members = "au.geekseat.com.hub3candroid:id/textLinkMembers"
    invite_member = "au.geekseat.com.hub3candroid:id/textLinkInviteMembers"

    def __init__(self, driver):
        self.driver = driver

    def verified_all_element(self):
        try:
            WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.ID, self.connected)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.pending)))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, self.request)))
            print("Dadshboard page is compleately loaded")
        except TimeoutException:
            print("element not ready")

    def tap_notifications(self):
        pass

    def tap_connected_business(self):
        self.driver.find_element_by_id(self.connected).click()

    def tap_pending_invitations(self):
        pass

    def tap_connect_request(self):
        pass

    def tap_invite_more_business(self):
        pass

    def tap_members(self):
        pass

    def tap_invite_team_members(self):
        pass

