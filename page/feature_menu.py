from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Feature():

    loc_network_name = "Network"
    loc_job2job_name = "Job2Job"
    loc_prject_name = "Project"
    loc_image_xpath = '//XCUIElementTypeApplication[@name="Hub3c"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeImage'
    loc_close_id = "Close"
    loc_cell_header = '//XCUIElementTypeApplication[@name="Hub3c"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]'

    def __init__(self, driver):
        self.driver = driver

    def tap_business_network(self):
        pass

    def tap_projects(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, self.loc_prject_name)))
        except TimeoutException:
            print("Project module not found")

        self.driver.find_element_by_xpath(self.loc_prject_name).click()

    def tap_job2job(self):
        pass

    def tap_header(self, user_name=None):

        if user_name == None:
            try:
                WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.XPATH, self.loc_cell_header)))
            except TimeoutException:
                print("ERRAWR : Somehow header is not located, check element locator !!")
            self.driver.find_element_by_xpath(self.loc_cell_header).click()

        else:
            # locator = "//XCUIElementTypeStaticText[@name='{}']".format(user_name)
            try:
                WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((By.ID, user_name)))
            except TimeoutException:
                print("ERRAWR : Somehow header is not located, check element locator !!")
            self.driver.find_element_by_id(user_name).click()

        print("Tap Header")




    def tap_arrow_nav(self):
        pass

    def tap_cencel(self):
        pass



''' alternative locator '''

# au.geekseat.com.hub3candroid:id/sideProject
# au.geekseat.com.hub3candroid:id/imageProject
# au.geekseat.com.hub3candroid:id/sideNavBusiness
# au.geekseat.com.hub3candroid:id/imageBusinessNetwork