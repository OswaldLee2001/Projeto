#!/usr/bin/env python3
#!-*-coding:utf-8-*-

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.estantevirtual.com.br/")
print(driver.title)
driver.quit()
