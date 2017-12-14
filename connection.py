from appium import webdriver

class Connection():

    desired_caps = {}
    desired_caps['platformName'] = 'iOS'
    desired_caps['platformVersion'] = '11.2'
    desired_caps['deviceName'] = 'iPhone 6s'
    desired_caps['automationName'] = 'XCUITest'
    desired_caps['noReset'] = False
    desired_caps['fullReset'] = False
    desired_caps['bundleId'] = 'com.geekseat.Hub3c'
    # desired_caps['app'] = '/Users/geekseat/Desktop/hub3c.ipa'

    ## ###### emulator SE
    # desired_caps['udid'] = '49448AA7-E917-44A9-96E9-EE13E28067F0'

    ## ###### emulator 6s
    # desired_caps['udid'] = 'A91FB5C3-F077-4B5C-A573-CCC6D3D3CE7A'

    ### ####### real devices additional configuration
    desired_caps['udid'] = 'e565b81cc6d621b8faaea1b23fc3e6c707a2a0fb'
    desired_caps['xcodeOrgId'] = "hub Global Pte Ltd"
    desired_caps['xcodeSigningId'] = "iPhone Developer"

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


