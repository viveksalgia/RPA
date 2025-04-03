#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# Project - Burden_Build
# Filename - logout.py
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

from stripui.get_tag_id import get_ids, get_anchor_id
import time


def inputs(driver, elementid, value):
    search = driver.find_element(By.ID, elementid)
    search.send_keys(value)


def logout(driver):
    """Execute the script."""

    # Get id for Userid field
    id = get_ids(driver.page_source, "title", "Settings and Actions", 0, "id")
    inputs(driver, id, Keys.RETURN)

    time.sleep(3)

    id = get_anchor_id(
        driver.page_source,
        "a",
        "Sign Out",
        0,
        "id",
    )
    # print("Sign Out Id is - " + id)
    inputs(driver, id, Keys.RETURN)
