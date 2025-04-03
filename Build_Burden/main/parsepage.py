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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from stripui.get_tag_id import get_ids, get_anchor_id


def inputs(driver, elementid, value):
    search = driver.find_element(By.ID, elementid)
    search.send_keys(value)


def parseLoc(driver):

    # driver.delete_all_cookies()

    # Click on the Navigator
    try:
        id = get_ids(driver.page_source, "title", "Navigator", 0, "id")
        inputs(driver, id, Keys.RETURN)
    except:
        raise Exception("Unable to click on Navigator")

    time.sleep(2)

    # Expand Grants Management
    try:
        id = get_ids(driver.page_source, "title", "Grants Management", 0, "id")
        ActionChains(driver).move_to_element(driver.find_element(By.ID, id)).click(
            driver.find_element(By.ID, id)
        ).perform()
    except:
        raise Exception("Unable to click on Grants Management")
    time.sleep(2)

    # Click on Awards
    try:
        id = get_ids(driver.page_source, "title", "Awards", 0, "id")
        ActionChains(driver).move_to_element(driver.find_element(By.ID, id)).click(
            driver.find_element(By.ID, id)
        ).perform()
    except:
        raise Exception("Unable to click on Awards")
    time.sleep(2)


def update_award(driver, project_number, award_number, project_name):

    # Click on Actions Side Icon
    try:
        id = get_ids(driver.page_source, "title", "Actions", 1, "id")
        ActionChains(driver).move_to_element(driver.find_element(By.ID, id)).click(
            driver.find_element(By.ID, id)
        ).perform()
    except:
        raise Exception("Unable to Open Actions")

    # Wait for Action Side Icon to open and move the focus to that frame
    driver.implicitly_wait(2)
    driver.switch_to.frame

    time.sleep(2)

    # Click on the List Item 'Manage Awards'
    """WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="_FOpt1:_FOr1:0:_FONSr2:0:_FOTsr1:0:r1:0:AP1:commandLink3"]',
            )
        )
    ).send_keys(Keys.RETURN)"""
    # Click on the Manage Awards
    try:
        id = get_anchor_id(
            driver.page_source,
            "a",
            "Manage Awards",
            0,
            "id",
        )

        # print("*********** - " + id + " - ***************")

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    id,
                )
            )
        ).send_keys(Keys.RETURN)
    except:
        raise Exception("Unable to click on Manage Awards")

    time.sleep(5)

    # Go to the search box and enter the project number and search for the project
    try:
        id = get_ids(
            driver.page_source,
            "name",
            "_FOpt1:_FOr1:0:_FONSr2:0:_FOTsr1:0:r3:1:ph1:ffs2:fs_keywordSearchBox",
            0,
            "id",
        )
        inputs(driver, id, project_number)
        inputs(driver, id, Keys.RETURN)
    except:
        raise Exception(
            "Unable to enter the project number to search project and award"
        )

    time.sleep(2)

    # Click on the Award
    try:
        id = get_anchor_id(
            driver.page_source,
            "a",
            award_number,
            0,
            "id",
        )

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    id,
                )
            )
        ).send_keys(Keys.RETURN)
    except:
        raise Exception("Unable to click on Award Number to enter the Award screen")
    time.sleep(2)

    # Click on the Edit Award
    try:
        id = get_ids(driver.page_source, "title", "Edit Award", 0, "id")
        ActionChains(driver).move_to_element(driver.find_element(By.ID, id)).click(
            driver.find_element(By.ID, id)
        ).perform()
    except:
        raise Exception("Unable to click on Edit Award")

    # Wait for Action Side Icon to open and move the focus to that frame
    """driver.implicitly_wait(10)
    driver.switch_to.frame"""

    # Click on the train stop Projects
    try:
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="_FOpt1:_FOr1:0:_FONSr2:0:_FOTsr1:1:pt1:pt2:AP3:pt_t1:1:_afrStopNavItem"]/div[2]/a',
                )
            )
        ).send_keys(Keys.RETURN)
    except:
        raise Exception("Unable to click on train stop for Projects")

    time.sleep(2)

    try:
        id = get_ids(
            driver.page_source,
            "name",
            "_afrFilter_FOpt1_afr__FOr1_afr_0_afr__FONSr2_afr_0_afr__FOTsr1_afr_2_afr_pt1_afr_awdPrj2_afr_AP3_afr_r1_afr_0_afr_pc1_afr__ATp_afr_t3_afr_c1",
            0,
            "id",
        )
    except:
        # Click on the filter to enter project
        id = get_ids(driver.page_source, "title", "Query By Example", 0, "id")
        ActionChains(driver).move_to_element(driver.find_element(By.ID, id)).click(
            driver.find_element(By.ID, id)
        ).perform()

    time.sleep(2)

    # Click enter project number in the filter
    try:
        id = get_ids(
            driver.page_source,
            "name",
            "_afrFilter_FOpt1_afr__FOr1_afr_0_afr__FONSr2_afr_0_afr__FOTsr1_afr_2_afr_pt1_afr_awdPrj2_afr_AP3_afr_r1_afr_0_afr_pc1_afr__ATp_afr_t3_afr_c1",
            0,
            "id",
        )
        inputs(driver, id, project_number)
        inputs(driver, id, Keys.RETURN)
    except:
        raise Exception("Unable to click on filter on the project")

    time.sleep(5)

    # Click to expand the project details
    try:
        id = get_ids(
            driver.page_source, "title", "Expand " + project_name + ": Details", 0, "id"
        )
        ActionChains(driver).move_to_element(driver.find_element(By.ID, id)).click(
            driver.find_element(By.ID, id)
        ).perform()
    except:
        raise Exception("Unable to expand the project details")

    time.sleep(2)

    # Click on the Financial Information
    try:
        id = get_anchor_id(
            driver.page_source,
            "a",
            "Financial",
            0,
            "id",
        )

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    id,
                )
            )
        ).send_keys(Keys.RETURN)
    except:
        raise Exception("Unable to click on Project Financial Information Tab")

    time.sleep(2)

    # Click on the Award
    try:
        """id = get_anchor_id(
            driver.page_source,
            "a",
            award_number + " - " + project_number,
            0,
            "id",
        )"""

        id = get_ids(
            driver.page_source, "title", "Manage Override Burden Schedule", 0, "id"
        )

        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    id,
                )
            )
        ).send_keys(Keys.RETURN)
    except:
        id = get_ids(
            driver.page_source, "title", "Create Override Burden Schedule", 0, "id"
        )
        ActionChains(driver).move_to_element(driver.find_element(By.ID, id)).click(
            driver.find_element(By.ID, id)
        ).perform()

    # Wait for Action Side Icon to open and move the focus to that frame
    # driver.implicitly_wait(10)
    # driver.switch_to.frame

    time.sleep(2)

    try:
        id = get_anchor_id(
            driver.page_source,
            "button",
            "Build Burden Schedule",
            0,
            "id",
        )

        # Click on the train stop Projects
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    id,
                )
            )
        ).send_keys(Keys.RETURN)
    except:
        raise Exception("Unable to click on Build Burden Schedule button")

    time.sleep(5)

    try:
        id = get_anchor_id(
            driver.page_source,
            "button",
            "OK",
            0,
            "id",
        )
    except:
        id = get_anchor_id(
            driver.page_source,
            "button",
            'accesskey="K"',
            -99,
            "id",
        )
    WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable(
            (
                By.ID,
                id,
            )
        )
    ).send_keys(Keys.RETURN)

    # Click on save and close
    try:
        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    id,
                )
            )
        ).send_keys(Keys.RETURN)
    except:
        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="_FOpt1:_FOr1:0:_FONSr2:0:_FOTsr1:2:pt1:awdPrj2:AP3:r1:0:r1:0:r1:0:bschat:cb3"]',
                )
            )
        ).send_keys(Keys.RETURN)
    else:
        raise Exception("Unable to click OK")

        time.sleep(2)

    try:
        id = get_anchor_id(
            driver.page_source,
            "button",
            "Save and Close",
            0,
            "id",
        )
        # Click on Save and Next
        WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    id,
                )
            )
        ).send_keys(Keys.RETURN)
    except:
        raise Exception("Unable to click Save and Close")

        time.sleep(2)

    try:

        id = get_anchor_id(
            driver.page_source,
            "button",
            "Save and Next",
            0,
            "id",
        )
        # Click on the train stop Projects
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    id,
                )
            )
        ).click()
    except:
        return "Unable to click Save and Next"

    time.sleep(2)

    # id = get_ids(driver.page_source, "accesskey", "o", 0, "id")

    # print("******* - " + id + " - ***********")

    # Click on the done
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="_FOpt1:_FOr1:0:_FONSr2:0:_FOTsr1:3:pt1:mgtFuns:AP3:pt_ctb2"]',
                )
            )
        ).click()
    except:
        return "Unable to click on Done editing the Award"

    time.sleep(1)

    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="_FOpt1:_FOr1:0:_FONSr2:0:_FOTsr1:0:r2:0:ASumAP1:ctb1"]',
                )
            )
        ).click()
    except:
        return "Unable to click on Done viewing the Award"

    time.sleep(1)

    # Click on Actions Side Icon
    try:
        id = get_ids(driver.page_source, "title", "Actions", 1, "id")
        ActionChains(driver).move_to_element(driver.find_element(By.ID, id)).click(
            driver.find_element(By.ID, id)
        ).perform()
    except:
        return "Unable close the actions section"

    return "Burden Version Built Successfully"
