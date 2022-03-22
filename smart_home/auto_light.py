#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: auto_light.py
# @Author: 檀寅
# @Time: 2022年03月15日16:25
# @说明:
from xaal.lib import Engine, helpers, AsyncEngine, tools
from xaal.schemas import devices
import asyncio

helpers.set_console_title("xaal-dumper")

ADDR_KITCHEN_ZONE = "9963210a-d5ba-11eb-aaa7-cc483ac19e2d"
ADDR_BATHROOM_ZONE = "9d268b24-d5ba-11eb-aaa7-cc483ac19e2d"
ADDR_SOFA_PRESSURE = "039593e0-d3ff-11eb-ba59-fc44827cb3d9"
ADDR_BED_PRESSURE = "0df9219e-d3ff-11eb-ba59-fc44827cb3d9"

ADDR_LIGHT_KITCHEN = "ccc44227-d4fc-46eb-8578-159e2c47da04"
ADDR_LIGHT_BATHROOM = "ccc44227-d4fc-46eb-8578-159e2c47da06"
ADDR_SCREEN = "2d42a742-aa2f-11e9-ac3b-a4badbf92501"
ADDR_SHUTTER = "2fe70f46-3ece-44d1-af34-2d82e10fb854"

DURATION_TV = 1 * 5
DURATION_LIGHT_KITCHEN = 1 * 5
DURATION_LIGHT_BATHROOM = 1 * 5
DURATION_SHUTTER = 1 * 10


def display(msg):
    print(msg.body.keys())


async def light_kitchen_auto(msg):
    if str(msg.source) == ADDR_KITCHEN_ZONE:
        if "presence" in msg.body.keys():
            # print(msg.body["presence"])
            # print(type(msg.body["presence"]))
            if msg.body["presence"]:
                eng.send_request(dev, [tools.get_uuid(ADDR_LIGHT_KITCHEN)], "turn_on")
            else:
                await asyncio.sleep(DURATION_LIGHT_KITCHEN)
                eng.send_request(dev, [tools.get_uuid(ADDR_LIGHT_KITCHEN)], "turn_off")


async def light_bathroom_auto(msg):
    if str(msg.source) == ADDR_BATHROOM_ZONE:
        if "presence" in msg.body.keys():
            if msg.body["presence"]:
                eng.send_request(dev, [tools.get_uuid(ADDR_LIGHT_BATHROOM)], "turn_on")
            else:
                await asyncio.sleep(DURATION_LIGHT_BATHROOM)
                eng.send_request(dev, [tools.get_uuid(ADDR_LIGHT_BATHROOM)], "turn_off")


async def turn_tv_auto(msg):
    if str(msg.source) == ADDR_SOFA_PRESSURE:
        if "detected" in msg.body.keys():
            if msg.body["detected"]:
                eng.send_request(dev, [tools.get_uuid(ADDR_SCREEN)], "turn_on")
            else:
                await asyncio.sleep(DURATION_TV)
                eng.send_request(dev, [tools.get_uuid(ADDR_SCREEN)], "turn_off")


async def turn_shutter_auto(msg):
    if str(msg.source) == ADDR_BED_PRESSURE:
        if "detected" in msg.body.keys():
            if msg.body["detected"]:
                eng.send_request(dev, [tools.get_uuid(ADDR_SHUTTER)], "down")
            else:
                await asyncio.sleep(DURATION_SHUTTER)
                eng.send_request(dev, [tools.get_uuid(ADDR_SHUTTER)], "up")


def main():
    try:
        global eng
        global dev
        dev = devices.basic()
        eng = AsyncEngine()
        eng.add_device(dev)

        eng.subscribe(light_kitchen_auto)
        eng.subscribe(light_bathroom_auto)
        eng.subscribe(turn_tv_auto)
        eng.subscribe(turn_shutter_auto)

        eng.disable_msg_filter()
        eng.run()
    except KeyboardInterrupt:
        print("Bye Bye")


if __name__ == '__main__':
    main()
