from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from PIL import Image
import logging
import psutil
import json
import time
import csv
import sys
import os

    
extra_big_delay = 20
big_delay = 12 
med_delay = 8
low_delay = 5


logging_conf = "=== %(asctime)s || %(levelname)s ||  %(lineno)d --- %(message)s  ==="
log_file_name = "error_tracking.txt"

logFormatter = logging.Formatter(logging_conf)
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler(log_file_name)
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
rootLogger.setLevel(logging.INFO)


options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox( service=Service(GeckoDriverManager().install()) , options=options)
driver.maximize_window()

url = 'https://www.instagram.com/'

email = 'putyourownemailandpassword@mail.com'
passwd = 'passwordhere'

driver.get (url)
# keyword = 'Air Duct Cleaning florida'
############################################################
time.sleep (med_delay)

login_entry_xpath = '(//*[@class="_2hvTZ pexuQ zyHYP"])[1]'
try:
    login_entry = driver.find_element (By.XPATH,login_entry_xpath)
    login_entry.send_keys(email)
except Exception as E:
    rootLogger.error(f'Failed to enter email due to {E}')

time.sleep (2)

password_entry_xpath = '(//label[@class="f0n8F "]/input)[2]'
try:
    passwd_entry = driver.find_element (By.XPATH,password_entry_xpath)
    passwd_entry.send_keys(passwd)
except Exception as E:
    rootLogger.error(f'Failed to enter passwd due to {E}')

time.sleep (2)

login_btn_xpath = '//button[@class="sqdOP  L3NKy   y3zKF     "]'
try:
    login_btn = driver.find_element (By.XPATH,login_btn_xpath)
    login_btn.click()
except Exception as E:
    rootLogger.error(f'Failed to login due to {E}')

time.sleep (med_delay)
############################################################

file_name = 'Screenshot.png'
driver.save_screenshot(file_name)
image = Image.open(file_name)
image.show()  
# ###################   

driver.quit ()
PROCNAME = "geckodriver" # or chromedriver or IEDriverServer
for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME:
        proc.kill()
try:
    os.system("taskkill /f /im geckodriver.exe /T")
    # os.system("taskkill /f /im firefox.exe /T")
except:
    pass
exit ()