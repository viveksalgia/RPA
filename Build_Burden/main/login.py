#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# Project - Burden_Build
# Filename - login.py
# Arguments - html
# Created By - Vivek Salgia
# Creation Date - 08/26/2024
# Reviewed By -
# Reviewed Date -
# Change logs -
# Version   Date         Type   Changed By                  Comments
# =======   ============ ====   ==============  ===============================
# 1.0       26-Aug-2024   I     Vivek Salgia    Initial Creation
###############################################################################
import logging
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from stripui.get_tag_id import get_ids
import time


def inputs(driver, elementid, value):
    search = driver.find_element(By.ID, elementid)
    search.send_keys(value)


def login(url, args):
    """Execute the script."""
    url = args.url

    url_user = "oicserviceaccount"
    url_pass = "Broad123!"

    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.get(url)

    time.sleep(5)

    # Get id for Userid field
    id = get_ids(driver.page_source, "name", "userid", 0, "id")
    inputs(driver, id, url_user)

    id = get_ids(driver.page_source, "name", "password", 0, "id")
    inputs(driver, id, url_pass)

    driver.implicitly_wait(10)
    inputs(driver, "btnActive", Keys.RETURN)
    driver.implicitly_wait(10)

    return driver
