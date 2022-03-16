#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: i.py
# @Author: 檀寅
# @Time: 2022年03月15日16:38
# @说明: 

from xaal.lib import Device, Engine, tools
from math import sqrt

# create and configure the lamp device, with a random address
dev = Device("thermometer.basic", tools.get_random_uuid())
dev.product_id = 'Rosee'
dev.url = 'http://www.acme.org'
dev.info = 'A Device to give the rosee temperature'

# add an xAAL attribute 'temperature_dewpoint'
temperature_dewpoint = dev.new_attribute('temperature_dewpoint')

#  attribute to update dewpoint
temperature_ambiante = None
humidity = None

temperature_addr = "1c344e46-9939-11ec-9856-080027ba0e00"
humidity_addr = "1c344e46-9939-11ec-9856-080027ba0e01"


# update dewpoint temperature
def update_dewpoint():
    if temperature_ambiante is None or humidity is None:
        return

    t = temperature_ambiante
    phi = humidity
    temperature_dewpoint.value = phi ** (1 / 8) * (112 + 0.9 * t) + 0.1 * t - 112
    print("dewpoint temperature value : ", temperature_dewpoint.value)


def display(msg):
    global temperature_ambiante
    global humidity

    if str(msg.source) == temperature_addr and msg.is_attributes_change():
        temperature_ambiante = msg.body['temperature']
        update_dewpoint()
    elif str(msg.source) == humidity_addr and msg.is_attributes_change():
        humidity = (msg.body['humidity'] / 100.0)
        update_dewpoint()


# last step, create an engine and register the lamp
eng = Engine()
eng.disable_msg_filter()
eng.add_device(dev)
eng.subscribe(display)
eng.run()
