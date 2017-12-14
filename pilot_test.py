from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['appiumVersion'] = '1.7'
desired_caps['platformVersion'] = '11.2'
desired_caps['deviceName'] = 'iPhone 6s'
desired_caps['automationName'] = 'XCUITest'
# desired_caps['app'] = '/Users/geekseat/Desktop/hub3c.ipa'
desired_caps['bundleId'] = 'com.geekseat.Hub3c'
desired_caps['udid'] = '49448AA7-E917-44A9-96E9-EE13E28067F0'

el_login = "//XCUIElementTypeApplication[@name='Hub3c']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
login = driver.find_element_by_xpath(el_login)

print(login)
