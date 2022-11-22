# RSIBotCop - main.py
# Version 1.0
# Created by Cyanox - https://github.com/Cyanox
# 09/10/2022

import os
import json
import random
import math

import pickle
import time

import selenium
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from const import options, CREDIT_CARD, SHIP_URL, LOGINS

PATH_DRIVER = os.path.join(os.curdir, 'chromedriver')


def main():
    driver = webdriver.Chrome(PATH_DRIVER, options=options)
    driver.get(SHIP_URL)
    signin(driver, LOGINS)
    driver.get(SHIP_URL)
    try:
        driver.find_element(By.ID, 'allow-selected').click()
    except:
        pass
    add_to_basket(driver)


def add_to_basket(driver):

    driver.find_element(By.XPATH, '//main[contains(@class, "ItemWidget")]/div[.//h3[not(contains(., "Warbond"))]]/following-sibling::div/button/div').click()

# def finalizing_order(driver, CREDIT_CARD):


def signin(driver, login):
    driver.find_element(By.CSS_SELECTOR, 'a[href="/account/settings"]').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'input[id="email"]').send_keys(login["mail"])
    driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').send_keys(login["password"])
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


if __name__ == "__main__":
    main()
