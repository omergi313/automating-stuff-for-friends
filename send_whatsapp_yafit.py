# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:09:32 2020

@author: omerg
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys


#initiate 
driver = webdriver.Firefox()


print('Hi Yafit!!!')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 120)


#get numbers
targets = open('OGnums.txt','r').read().split('\n')
#fix number like whatsapp's template
targets = ['"'+t[:4]+' '+t[4:6]+'-'+t[6:9]+'-'+t[9:]+'"' for t in targets]




string = input('Message:  ')

if input('Sure?    (yes/no)') == 'yes/no':

    #send to each number in list
    for target in targets:
        #look for the contact by number
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()
        
        
        #find messaging element
        message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        message.send_keys(string)
        
        
        sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
        sendbutton.click()
        
        
else:
    print('stom')


driver.close()