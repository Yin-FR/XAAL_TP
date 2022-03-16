#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: func.py
# @Author: 檀寅
# @Time: 2022年03月01日11:22
# @说明: 

import datetime

def get_yesterday():
    today = datetime.date.today()

    yesterday = today - datetime.timedelta(days=1)
