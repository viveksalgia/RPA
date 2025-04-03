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
from lxml import etree

# import requests


def get_ids(urlHTML, attrname, attrvalue, attrarraynum, gettag):
    soup = BeautifulSoup(urlHTML, "html.parser")
    print(soup.find(attrs={attrname: attrvalue}))
    id_tag = soup.find_all(attrs={attrname: attrvalue})

    return id_tag[attrarraynum].get(gettag)


def get_anchor_id(urlHTML, attrname, attrvalue, attrarraynum, gettag):
    soup = BeautifulSoup(urlHTML, "html.parser")
    for div in soup.find_all("div", attrs={attrname: attrvalue}):
        print(div.find("a").contents[attrarraynum])
        print(div.find("a").get(gettag))


if __name__ == "__main__":
    RET = get_ids(
        "https://fa-eujh-test-saasfaprod1.fa.ocs.oraclecloud.com/biacm",
        "name",
        "userid",
        0,
    )
    print(RET)
