from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Feature():

    business = "//*[@text='Business network']"
    job2job = "au.geekseat.com.hub3candroid:id/sideNavJob2job"
    project = "//*[@text='Projects']"
    profile_picture = "au.geekseat.com.hub3candroid:id/imageProfile"
    header = "au.geekseat.com.hub3candroid:id/containerSideNavHeader"
    arrow_nav = "(//*[@id='sideNavHeader']/*[@class='android.widget.ImageView'])[2]"
    cancel = "au.geekseat.com.hub3candroid:id/edit_cancel"

    def __init__(self, driver):
        self.driver = driver

    def tap_business_network(self):
        pass

    def tap_projects(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.project)))
            self.driver.find_element_by_xpath(self.project).click()
        except TimeoutException:
            print("Project module not found")

    def tap_job2job(self):
        pass

    def tap_header(self):

        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, self.profile_picture)))
            self.driver.find_element_by_id(self.profile_picture).click()
        except TimeoutException:
            print("element not ready")

    def tap_arrow_nav(self):
        pass

    def tap_cencel(self):
        pass



''' alternative locator '''

# au.geekseat.com.hub3candroid:id/sideProject
# au.geekseat.com.hub3candroid:id/imageProject
# au.geekseat.com.hub3candroid:id/sideNavBusiness
# au.geekseat.com.hub3candroid:id/imageBusinessNetwork