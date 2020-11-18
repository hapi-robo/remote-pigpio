#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Remotely control light

"""
import sys
import pigpio

from time import sleep


# remote host parameters
# HOSTNAME = '192.168.0.128' # test-bench
# HOSTNAME = '192.168.0.152' # robot
HOSTNAME = '192.168.0.194' # fongpi
PORT = 8888

# PIGPIO parameters
GPIO_PIN = 17 # https://pinout.xyz/pinout/pin11_gpio17#


def push_button(pin):
    pi.write(pin, 0)
    sleep(0.2)
    pi.write(pin, 1)


if __name__ == "__main__":
    pi = pigpio.pi(HOSTNAME, PORT)

    # exit script if unable to connect to remote host
    if not pi.connected:
        print("Unable to connect to {}:{}".format(HOSTNAME, PORT))
        sys.exit(1)

    # set gpio modes
    pi.set_mode(GPIO_PIN, pigpio.OUTPUT)
    pi.set_pull_up_down(GPIO_PIN, pigpio.PUD_UP)
    sleep(1)

    while True:
        # side lights
        push_button(GPIO_PIN)
        sleep(0.2)
        push_button(GPIO_PIN)
        sleep(1)

        # center light (low-power)
        push_button(GPIO_PIN)
        sleep(1)

        # center light (high-power)
        push_button(GPIO_PIN)
        sleep(1)

        # center light (blink)
        push_button(GPIO_PIN)
        sleep(3)

        # off
        push_button(GPIO_PIN)
        sleep(3)

    pi.stop()
