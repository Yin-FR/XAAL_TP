#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: dev.py
# @Author: 檀寅
# @Time: 2022年03月01日15:30
# @说明:
import aioesphomeapi
from xaal.lib import Device


class MyRelay(Device):
    def __init__(self, key, info, addr=None):
        super().__init__(dev_type="powerrelay.basic", addr=addr)
        self.new_attribute("power", False)
        self.product_id = "relay yin"
        self.info = info
        self.add_method("turn_on", self.turn_on)
        self.add_method("turn_off", self.turn_off)
        self.key = key

    async def turn_on(self):
        cli = aioesphomeapi.APIClient("sonoff1", 6053, password="MyPassword")
        await cli.connect(login=True)
        await cli.switch_command(self.key, True)

    async def turn_off(self):
        cli = aioesphomeapi.APIClient("sonoff1", 6053, password="MyPassword")
        await cli.connect(login=True)
        await cli.switch_command(self.key, False)


class MySensor(Device):
    def __init__(self, dev_type="mysensor.basic", addr=None):
        super().__init__(dev_type=dev_type, addr=addr)
        self.new_attribute("sensor", 0)
        self.product_id = "sensor"
        self.info = "sensor"


class MySensorZone(Device):
    def __init__(self, dev_type="motion.basic", addr=None):
        super().__init__(dev_type=dev_type, addr=addr)
        self.new_attribute("presence", default=False)