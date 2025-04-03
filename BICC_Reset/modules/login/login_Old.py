#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# Project - Reset BICC
# Filename - login.py
# Arguments - html
# Created By - Vivek Salgia
# Creation Date - 06/03/2024
# Reviewed By -
# Reviewed Date -
# Change logs -
# Version   Date         Type   Changed By                  Comments
# =======   ============ ====   ==============  ===============================
# 1.0       12-Dec-2022   I     Vivek Salgia    Initial Creation
###############################################################################
import logging
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from get_tag_id import get_ids


def inputs(driver, elementid, value):
    search = driver.find_element(By.ID, elementid)
    search.send_keys(value)


def login(url, args):
    """Execute the script."""
    url = args.url

    # Set the logging defaults for all inherited logging calls
    logging.basicConfig(level=logging.getLevelName(args.loglevel.upper()))
    url_user = "informaticaserviceaccount"
    url_pass = "KqUxXaW3WTHD"

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

    # Get id for Userid field
    id = get_ids(driver.page_source, "name", "userid", 0, "id")
    inputs(driver, id, url_user)

    id = get_ids(driver.page_source, "name", "password", 0, "id")
    inputs(driver, id, url_pass)

    driver.implicitly_wait(10)
    inputs(driver, "btnActive", Keys.RETURN)
    driver.implicitly_wait(10)

    return driver
