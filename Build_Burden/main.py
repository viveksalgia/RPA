###############################################################################
# Project - Burden_Build
# Filename - main.py
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
import argparse
import logging
import os
import sys
from selenium import webdriver
import time
import pandas as pd
import traceback

from main.login import login
from main.parsepage import parseLoc, update_award
from main.logout import logout

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
    logger = logging.getLogger(__name__)

    # do_reset(driver)

    csvFile = pd.read_csv("config/data.csv")

    projectList = csvFile["PROJECT_NUMBER"].to_list()
    awardList = csvFile["AWARD_NUMBER"].to_list()
    projectName = csvFile["PROJECT_NAME"].to_list()
    prjList = []
    awdList = []
    prjNmList = []
    statusList = []
    messageList = []

    for i in range(len(projectList)):
        try:
            driver = login(url, args)
            time.sleep(2)
            retMsg = parseLoc(driver)
            # print(str(projectList[i]) + "," + str(awardList[i]) + "," + str(projectName[i]))
            retMsg = update_award(
                driver, str(projectList[i]), str(awardList[i]), str(projectName[i])
            )
            time.sleep(2)
            logout(driver)
            time.sleep(3)
            driver.close
            prjList.append(str(projectList[i]))
            awdList.append(str(awardList[i]))
            prjNmList.append(str(projectName[i]))
            statusList.append("SUCCESS")
            messageList.append(retMsg)
        except Exception as e:
            traceback.print_exc
            driver.close
            prjList.append(str(projectList[i]))
            awdList.append(str(awardList[i]))
            prjNmList.append(str(projectName[i]))
            statusList.append("ERROR")
            messageList.append(str(e))
            continue

    with pd.ExcelWriter("config/output.xlsx") as writer:
        dfdata = {
            "PROJECT_NUMBER": prjList,
            "AWARD_NUMBER": awdList,
            "PROJECT_NAME": prjNmList,
            "STATUS": statusList,
            "MESSAGE": messageList,
        }
        dfHead = pd.DataFrame(dfdata)
        dfHead.to_excel(writer, sheet_name="Output")


if __name__ == "__main__":
    RET = main()

    sys.exit(RET)
