#!/usr/bin/env python3
#!-*-coding:utf-8-*-

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://www.estantevirtual.com.br/")
elem = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/header/div[2]/div/div[2]/form/div[2]/input")
elem.send_keys("Meridiano de Sangue")
time.sleep(1.5)
elem2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/header/div[2]/div/div[2]/form/div[2]/button")
elem2.click()

