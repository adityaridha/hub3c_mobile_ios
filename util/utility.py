import sys
import os
import time
from pathlib import Path
from datetime import datetime
root = Path(__file__).parents[1]   #get the root directory
root_model = str(root)
sys.path.append(root_model)

parent_directory = os.getcwd()
failed_screenshot_dir = parent_directory + "\\test_screenshot\\failed_screenshot\\"
success_screenshot_dir = parent_directory + "\\test_screenshot\\success_screenshot\\"

now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

class Helper():

    def __init__(self, driver):
        self.driver = driver

    def tap_first_result_auto_complete(self, element, index=1):
        print(index)
        x = element.location['x']
        y = element.location['y']
        height = element.size['height']
        width = element.size['width']
        target_x = x + (int(width/2))
        target_y1 = y + height + (40*index)
        target_y2 = y + height + (50*index)

        suggestion_cord = []
        suggestion_cord.append((target_x, target_y1))
        suggestion_cord.append((target_x, target_y2))

        self.driver.tap(suggestion_cord)

    def tap_spinner_options(self, spinner, index=1):
        spinner.click()
        self.tap_first_result_auto_complete(element=spinner, index=index)

    def swipe_to_buttom(self):
        time.sleep(1)
        try:
            self.driver.swipe(522, 800, 495, 100, 1000)
            print("swipe success")
        except :
            print("swipe failed")

    def get_failed_screenshot(self, test_name):
        self.driver.save_screenshot(failed_screenshot_dir + "{}-{}.png".format(now, test_name))

    def get_screenshot(self, test_name):
        self.driver.save_screenshot(success_screenshot_dir + "{}-{}.png".format(now, test_name))

