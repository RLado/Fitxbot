from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


url='https://w3.cezanneondemand.com/CezanneOnDemand/Account/LogIn'

def clock_in(user,passwd,timeout=120):
    #Set firefox to headless mode
    ffopt=webdriver.FirefoxOptions()
    ffopt.headless=True

    #Create web driver object and go to the URL
    browser=webdriver.Firefox(options=ffopt)
    browser.get(url)

    #Wait for page to load
    element_present=EC.presence_of_element_located((By.XPATH,'//button[@type="submit"]'))
    WebDriverWait(browser,timeout).until(element_present)

    #Write username and password
    browser.find_element(By.ID, 'Username').clear()
    browser.find_element(By.ID, 'Username').send_keys(user)
    browser.find_element(By.ID, 'Password').clear()
    browser.find_element(By.ID, 'Password').send_keys(passwd)
    #Log in
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    #Wait for page to load
    element_present=EC.presence_of_element_located((By.XPATH,'//*[@title="Haz clic para registrar tu Clock In"]'))
    WebDriverWait(browser,timeout).until(element_present)

    #Click on the clock in button
    browser.find_element(By.XPATH, '//*[@title="Haz clic para registrar tu Clock In"]').click()
    
    #Wait for page to load
    element_present=EC.presence_of_element_located((By.XPATH,'(//button[@type="button"])[2]'))
    WebDriverWait(browser,timeout).until(element_present)
    
    #Confirm
    browser.find_element(By.XPATH, '(//button[@type="button"])[2]').click()

    #Quit the browser
    browser.close()
    browser.quit()

    #Print log message
    print(f'Clocked in at: {str(datetime.datetime.now())}')

def clock_out(user,passwd,timeout=120):
    #Set firefox to headless mode
    ffopt=webdriver.FirefoxOptions()
    ffopt.headless=True

    #Create web driver object and go to the URL
    browser=webdriver.Firefox(options=ffopt)
    browser.get(url)

    #Wait for page to load
    element_present=EC.presence_of_element_located((By.XPATH,'//button[@type="submit"]'))
    WebDriverWait(browser,timeout).until(element_present)

    #Write username and password
    browser.find_element(By.ID, 'Username').clear()
    browser.find_element(By.ID, 'Username').send_keys(user)
    browser.find_element(By.ID, 'Password').clear()
    browser.find_element(By.ID, 'Password').send_keys(passwd)
    #Log in
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    #Wait for page to load
    element_present=EC.presence_of_element_located((By.XPATH,'//*[@title="Haz clic para el Clock Out"]'))
    WebDriverWait(browser,timeout).until(element_present)

    #Click on the clock in button
    browser.find_element(By.XPATH, '//*[@title="Haz clic para el Clock Out"]').click()

    #Wait for page to load
    element_present=EC.presence_of_element_located((By.XPATH,'(//button[@type="button"])[2]'))
    WebDriverWait(browser,timeout).until(element_present)

    #Confirm
    browser.find_element(By.XPATH, '(//button[@type="button"])[2]').click()

    #Quit the browser
    browser.close()
    browser.quit()

    #Print log message
    print(f'Clocked out at: {str(datetime.datetime.now())}')
