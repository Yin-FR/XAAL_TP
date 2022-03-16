#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: light.py
# @Author: 檀寅
# @Time: 2022年03月15日17:19
# @说明:


def search_for_light(lamps):
    for l in lamps:
        dev = mon.devices.get_with_addr(l)
        if dev:
            light = dev.attributes.get('light', None)
            if light:
                return True
    return False


def on_off_light(lamps):
    if search_for_light(lamps):
        send(lamps, 'turn_off')
        return False
    else:
        send(lamps, 'turn_on')
        return True
