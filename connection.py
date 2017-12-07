from appium import webdriver

class Connection():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.0'
    desired_caps['deviceName'] = 'Asus Zenfone 2'
    desired_caps['udid'] = '192.168.29.101:5555'
    desired_caps['appPackage'] = "au.geekseat.com.hub3candroid"
    desired_caps['appActivity'] = ".activities.SplashActivity"
    desired_caps['noReset'] = False
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['appiumVersion'] = '1.6.5'


    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)