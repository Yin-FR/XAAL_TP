#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: main.py
# @Author: 檀寅
# @Time: 2022年03月01日09:00
# @说明: 

from xaal.lib import Engine


def display(msg):
    print(msg)


if __name__ == '__main__':
    eng = Engine()
    eng.subscribe(display)
    eng.run()
