###############################################################################
# Project - Reset BICC
# Filename - main.py
# Arguments - html
# Created By - Vivek Salgia
# Creation Date - 06/03/2024
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
import time

from login import login
from reset import do_reset

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


def main():
    """Execute the script."""
    args = parse_arguments()
    url = args.url

    driver = login(url, args)
    do_reset(driver)
    time.sleep(2)


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
