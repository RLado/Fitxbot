from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import datetime


url='https://w3.cezanneondemand.com/CezanneOnDemand/Account/LogIn'

def clock_in(user,passwd,timeout=15):
    #Set firefox to headless mode
    ffopt=webdriver.FirefoxOptions()
    ffopt.headless=True

    #Create web driver object and go to the URL
    browser=webdriver.Firefox(executable_path='./geckodriver',options=ffopt)
    browser.get(url)

    #Write username and password
    browser.find_element_by_id('Username').clear()
    browser.find_element_by_id('Username').send_keys(user)
    browser.find_element_by_id('Password').clear()
    browser.find_element_by_id('Password').send_keys(passwd)
    #Log in
    browser.find_element_by_xpath('//button[@type="submit"]').click()

    #Wait for page to load
    element_present=EC.presence_of_element_located((By.XPATH,'//*[@title="Haz clic para registrar tu Clock In"]'))
    webdriver.support.ui.WebDriverWait(browser,timeout).until(element_present)

    #Click on the clock in button
    browser.find_element_by_xpath('//*[@title="Haz clic para registrar tu Clock In"]').click()
    #Confirm
    browser.find_element_by_xpath('(//button[@type="button"])[2]').click()

    #Quit the browser
    browser.close()
    browser.quit()

    #Print log message
    print(f'Clocked in at: {str(datetime.datetime.now())}')

def clock_out(user,passwd,timeout=15):
    #Set firefox to headless mode
    ffopt=webdriver.FirefoxOptions()
    ffopt.headless=True

    #Create web driver object and go to the URL
    browser=webdriver.Firefox(executable_path='./geckodriver',options=ffopt)
    browser.get(url)

    #Write username and password
    browser.find_element_by_id('Username').clear()
    browser.find_element_by_id('Username').send_keys(user)
    browser.find_element_by_id('Password').clear()
    browser.find_element_by_id('Password').send_keys(passwd)
    #Log in
    browser.find_element_by_xpath('//button[@type="submit"]').click()

    #Wait for page to load
    element_present=EC.presence_of_element_located((By.XPATH,'//*[@title="Haz clic para el Clock Out"]'))
    webdriver.support.ui.WebDriverWait(browser,timeout).until(element_present)

    #Click on the clock in button
    browser.find_element_by_xpath('//*[@title="Haz clic para el Clock Out"]').click()
    #Confirm
    browser.find_element_by_xpath('(//button[@type="button"])[2]').click()

    #Quit the browser
    browser.close()
    browser.quit()

    #Print log message
    print(f'Clocked out at: {str(datetime.datetime.now())}')
