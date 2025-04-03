#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# Project - Reset BICC
# Filename - reset.py
# Arguments - html
# Created By - Vivek Salgia
# Creation Date - 06/13/2024
# Reviewed By -
# Reviewed Date -
# Change logs -
# Version   Date         Type   Changed By                  Comments
# =======   ============ ====   ==============  ===============================
# 1.0       13-Jun-2024   I     Vivek Salgia    Initial Creation
###############################################################################
import argparse
import logging
import requests
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..strip.get_tag_id import get_ids, get_anchor_id


def do_reset(driver):

    id = get_ids(driver.page_source, "title", "Manage Jobs", 1, "id")

    ActionChains(driver).move_to_element(driver.find_element(By.ID, id)).click(
        driver.find_element(By.ID, id)
    ).perform()

    id = get_anchor_id(driver.page_source, "class", "x3q", 0, "id")

    ActionChains(driver).move_to_element(driver.find_element(By.ID, id)).click(
        driver.find_element(By.ID, id)
    ).perform()
