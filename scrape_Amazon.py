import os,time
import sys
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select    
from selenium import webdriver

def SetUpChromeOptions(webdriver):
    chrome_options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values': {
                'images': 1,    # turn off image loading
                'javascript':2   #turn off JavaScript loading    
                }
            ,'permissions.default.stylesheet':2  # turn off css loading
            }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome('/Users/daweizhang/Dropbox/study/client_project/chromedriver', options=chrome_options)
    return(driver)

# if __name__ == '__main__':
#     address = 'https://www.amazon.com'
#     driver = SetUpChromeOptions(webdriver)
#     driver.get(address)

# driver.quit()

# searchbox 
searchbox = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchbox.send_keys('waist extender\n')