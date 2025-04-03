#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# Project - Reset BICC
# Filename - get_tag_id.py
# Arguments - html
# Created By - Vivek Salgia
# Creation Date - 06/12/2024
# Reviewed By -
# Reviewed Date -
# Change logs -
# Version   Date         Type   Changed By                  Comments
# =======   ============ ====   ==============  ===============================
# 1.0       12-Jun-2024   I     Vivek Salgia    Initial Creation
###############################################################################
from bs4 import BeautifulSoup
import re

# import requests


def get_ids(urlHTML, attrname, attrvalue, attrarraynum, gettag):
    soup = BeautifulSoup(urlHTML, "html.parser")
    # print(soup.find(attrs={attrname: attrvalue}))
    id_tag = soup.find_all(attrs={attrname: attrvalue})

    return id_tag[attrarraynum].get(gettag)


def get_anchor_id(urlHTML, attrname, attrvalue, attrarraynum, gettag):
    soup = BeautifulSoup(urlHTML, "html.parser")
    div = soup.find_all(attrname)

    for index in div:
        if attrarraynum == -99:
            print(str(index))
        if str(index).find(attrvalue) != -1:
            splitStr = str(index).split()
            for i in splitStr:
                if str(i).find("id") != -1:
                    # print(str(i))
                    return str(i)[4:-1]

    return None
