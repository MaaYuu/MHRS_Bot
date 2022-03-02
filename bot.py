#import os
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import winsound
from selenium.common.exceptions import NoSuchElementException



#from selenium.webdriver.chrome.options import Options

#options = Options()
#options.add_argument("--disable-notifications")

driver = webdriver.Chrome()
driver.get('https://mhrs.gov.tr/vatandas/')


tc = '***'
passw = '***'

driver.implicitly_wait(10) # seconds

driver.find_element_by_id("LoginForm_username").send_keys(tc)
driver.find_element_by_id("LoginForm_password").send_keys(passw)

driver.find_element_by_class_name("ant-btn.ant-btn-teal.ant-btn-block").click()
driver.implicitly_wait(10) # seconds


driver.find_element_by_class_name("ant-card.randevu-card.hasta-randevu-card.mb-16.mr-16").click()
#driver.implicitly_wait(10) # seconds
time.sleep(2)
driver.find_element_by_class_name("ant-btn.randevu-turu-button.konuma-arama-button.ant-btn-lg").click()

# Klinik seçim bekletmesi
time.sleep(15)

# Find butonuna tıklama ve 10 saniye bekleme
driver.find_element_by_class_name("ant-btn.ant-btn-primary").click()
time.sleep(5)

while True:
    time.sleep(10)
    
    try:
        button_pop = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button")
        if 'OK' in button_pop.text:
            button_pop.click()
            time.sleep(5)
            driver.find_element_by_class_name("ant-btn.ant-btn-primary").click()
    except NoSuchElementException:
        winsound.PlaySound('Alarm.wav', winsound.SND_FILENAME)


