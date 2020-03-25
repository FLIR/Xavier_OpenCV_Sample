#!/usr/bin/python3

import os


BOSON_BUS = 10
BOSON_I2C_ADDR = 0x6C
CMD_REG = 0


def send_i2c(bus, address, reg, val):
    os.system(f'sudo i2cset -f -y {bus} {hex(address)} {hex(reg)} {hex(val)}')


def read_i2c(bus, address, reg):
    os.system(f'sudo i2cget -f -y {bus} {hex(address)} {hex(reg)}')


def send_packet(values):
    for val in values:
        send_i2c(BOSON_BUS, BOSON_I2C_ADDR, CMD_REG, val)


def send_ffc():
    values = [0x8E, 0x00, 0x12, 0xC0, 0xFF, 0xEE, 0x00, 0x05, 0x00, 0x07, 
            0xFF, 0xFF, 0xFF, 0xFF, 0x6C, 0x5E, 0xAE]
    send_packet(values)


if __name__ == '__main__':
    send_ffc()
