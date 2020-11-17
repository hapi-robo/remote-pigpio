#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test Motor

When using daemon, remember to set the environment variables:
export PIGPIO_ADDR=HOSTNAME
export PIGPIO_PORT=PORT (Default: 8888)

"""
import pigpio
import argparse

from time import sleep


# HOSTNAME = '192.168.0.128' # test-bench
HOSTNAME = '192.168.0.152' # raybot
PORT = 8888

GPIO_PIN = 17 # https://pinout.xyz/pinout/pin11_gpio17#


def push_button(pin):
    pi.write(pin, 0)
    sleep(0.2)
    pi.write(pin, 1)


if __name__ == "__main__":

    # PARSER = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    # PARSER.add_argument("duty_cycle", type=int, help="Duty-cycle [0-100]")
    # ARGS = PARSER.parse_args()

    pi = pigpio.pi(HOSTNAME, PORT)

    # exit script if unable to connect
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
