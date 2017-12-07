import time
from appium import webdriver
from faker import Factory

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0'
desired_caps['deviceName'] = 'G4AZGF00C729HT9'
desired_caps['appPackage'] = "au.geekseat.com.hub3candroid'"
desired_caps['appActivity'] = ".activities.SplashActivity'"
desired_caps['noReset'] = False
desired_caps['automationName'] = 'uiautomator2'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

fake = Factory.create()
business = fake.company()
first_name = fake.first_name()
last_name = fake.last_name()
email = first_name + "." + last_name + "@mailinator.com"

time.sleep(2)
register = driver.find_element_by_id('au.geekseat.com.hub3candroid:id/textForgotPassword')
x = register.location['x']
y = register.location['y']
positions = []
positions.append((x + 10, y))
positions.append((x + 20, y))
driver.tap(positions)
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/editBusinessName').send_keys('Appium automation {}'.format(business))
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/spinner_title').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("First name")').click() ### click spinner value dirty way
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/editFirstName').send_keys(first_name)
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/editLastName').send_keys(last_name)
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/spinner_timezone').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("Email")').click() ### click spinner value dirty way
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/editEmail').send_keys(email)
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/editEmailRepeat').send_keys(email)
driver.swipe(start_x=60, end_x=60, start_y=1094, end_y=500)
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/editPassword').send_keys('ZXasqw12')
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/editPasswordRepeat').send_keys('ZXasqw12')
terms = driver.find_element_by_id('au.geekseat.com.hub3candroid:id/checkTerms')
x = terms.location['x']
y = terms.location['y']
positions = []
positions.append((x + 10, y))
positions.append((x + 20, y))
driver.tap(positions)
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/buttonRegister').click()

