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
import time

LOGGER = logging.getLogger(os.path.basename(__file__))


def parse_arguments():
    """Parse command-line arguments using argparse."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-u",
        "--url",
        help="Application URL you want to login",
        required=True,
    )
    parser.add_argument(
        "-l",
        "--loglevel",
        help=(
            "The logging level to set. Valid values are:\n"
            "\tCRITICAL, ERROR, WARNING, INFO, DEBUG"
        ),
        default="ERROR",
    )

    return parser.parse_args()


def inputs(driver, elementid, value):
    search = driver.find_element(By.ID, elementid)
    search.send_keys(value)


def main():
    """Execute the script."""
    args = parse_arguments()
    url = args.url

    # Set the logging defaults for all inherited logging calls
    logging.basicConfig(level=logging.getLevelName(args.loglevel.upper()))
    url_user = "informaticaserviceaccount"
    url_pass = "KqUxXaW3WTHD"

    driver = webdriver.Chrome()
    driver.get(url)

    inputs(driver, "userid", url_user)
    inputs(driver, "password", url_pass)
    driver.implicitly_wait(10)
    inputs(driver, "btnActive", Keys.RETURN)
    driver.implicitly_wait(10)

    ActionChains(driver).move_to_element(
        driver.find_element(By.ID, "pt1:pt_sdi61::ti")
    ).click(driver.find_element(By.ID, "pt1:pt_sdi61::ti")).perform()

    ActionChains(driver).move_to_element(
        driver.find_element(By.ID, "pt1:pt_cl64")
    ).click(driver.find_element(By.ID, "pt1:pt_cl64")).perform()

    """Uncomment for ERP Test"""
    """ActionChains(driver).move_to_element(
        driver.find_element(By.ID, "pt1:r2:pt1:lpspc1:t1:4:b1")
    ).click(driver.find_element(By.ID, "pt1:r2:pt1:lpspc1:t1:4:b1")).perform()"""

    ActionChains(driver).move_to_element(
        driver.find_element(By.ID, "pt1:r2:pt1:lpspc1:t1:2:b1")
    ).click(driver.find_element(By.ID, "pt1:r2:pt1:lpspc1:t1:2:b1")).perform()

    """Uncomment for ERP Test"""
    """ActionChains(driver).move_to_element(
        driver.find_element(By.ID, "pt1:r2:pt1:lpspc1:t1:4:resetcm")
    ).click(driver.find_element(By.ID, "pt1:r2:pt1:lpspc1:t1:4:resetcm")).perform()"""

    ActionChains(driver).move_to_element(
        driver.find_element(By.ID, "pt1:r2:pt1:lpspc1:t1:2:resetcm")
    ).click(driver.find_element(By.ID, "pt1:r2:pt1:lpspc1:t1:2:resetcm")).perform()

    driver.implicitly_wait(10)
    driver.switch_to.frame

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='pt1:r2:pt1:lpspc1:d64_yes']/a"))
    ).send_keys(Keys.RETURN)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='d1_msgDlg_cancel']/a"))
    ).send_keys(Keys.RETURN)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='pt1:pt_np1']/div"))
    ).send_keys(Keys.RETURN)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='pt1:pt_cni1']"))
    ).send_keys(Keys.RETURN)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='Confirm']"))
    ).send_keys(Keys.RETURN)

    time.sleep(5)


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
