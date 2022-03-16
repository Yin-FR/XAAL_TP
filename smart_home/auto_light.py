#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: auto_light.py
# @Author: 檀寅
# @Time: 2022年03月15日16:25
# @说明:
from xaal.lib import Engine, helpers, AsyncEngine, tools
from xaal.schemas import devices

helpers.set_console_title("xaal-dumper")

addr_kitchen_zone = "9963210a-d5ba-11eb-aaa7-cc483ac19e2d"
addr_bathroom_zone = "9d268b24-d5ba-11eb-aaa7-cc483ac19e2d"
addr_sofa_pressure = "039593e0-d3ff-11eb-ba59-fc44827cb3d9"
addr_bed_pressure = "0df9219e-d3ff-11eb-ba59-fc44827cb3d9"

addr_light_kitchen = "ccc44227-d4fc-46eb-8578-159e2c47da04"
addr_light_bathroom = "ccc44227-d4fc-46eb-8578-159e2c47da06"
addr_screen = "2d42a742-aa2f-11e9-ac3b-a4badbf92501"
addr_shutter = "2fe70f46-3ece-44d1-af34-2d82e10fb854"


def display(msg):
    # if str(msg.source) == "87b387c2-20b5-11e9-b352-a4badbf92500":
    # msg.dump()
    print(msg.body.keys())


async def get_value_presence(msg):
    if str(msg.source) == addr_kitchen_zone:
        if "presence" in msg.body.keys():
            # print(msg.body["presence"])
            # print(type(msg.body["presence"]))
            if msg.body["presence"]:
                eng.send_request(dev, [tools.get_uuid(addr_light_kitchen)], "turn_on")
            else:
                eng.send_request(dev, [tools.get_uuid(addr_light_kitchen)], "turn_off")
    elif str(msg.source) == addr_bathroom_zone:
        if "presence" in msg.body.keys():
            # print(msg.body["presence"])
            # print(type(msg.body["presence"]))
            if msg.body["presence"]:
                eng.send_request(dev, [tools.get_uuid(addr_light_bathroom)], "turn_on")
            else:
                eng.send_request(dev, [tools.get_uuid(addr_light_bathroom)], "turn_off")
    elif str(msg.source) == addr_sofa_pressure:
        if "detected" in msg.body.keys():
            if msg.body["detected"]:
                eng.send_request(dev, [tools.get_uuid(addr_screen)], "turn_on")
            else:
                eng.send_request(dev, [tools.get_uuid(addr_screen)], "turn_off")
    elif str(msg.source) == addr_bed_pressure:
        if "detected" in msg.body.keys():
            if msg.body["detected"]:
                eng.send_request(dev, [tools.get_uuid(addr_screen)], "down")
            else:
                eng.send_request(dev, [tools.get_uuid(addr_screen)], "up")


def main():
    try:
        global eng
        global dev
        dev = devices.basic()
        eng = AsyncEngine()
        eng.add_device(dev)
        eng.subscribe(get_value_presence)
        eng.disable_msg_filter()
        eng.run()
    except KeyboardInterrupt:
        print("Bye Bye")


if __name__ == '__main__':
    main()
