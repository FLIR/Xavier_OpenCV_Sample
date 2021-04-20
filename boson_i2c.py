#!/usr/bin/python3

import os
import subprocess

BOSON_BUS = 10
BOSON_I2C_ADDR = 0x6C
CMD_REG = 0
UART_REG = 0x09
DISABLE = 0x02
ENABLE = 0x00
BYTES_RDY_REG = 0x12

def send_i2c(bus, address, reg, val):
    os.system(f'sudo i2cset -f -y {bus} {hex(address)} {hex(reg)} {hex(val)}')

def read_i2c(bus, address, reg):
    #os.system(f'sudo i2cget -f -y {bus} {hex(address)} {hex(reg)}')
    val = subprocess.check_output(f'sudo i2cget -f -y {bus} {hex(address)} {hex(reg)}', stderr=subprocess.STDOUT, shell=True)
    return int(val, base=16)

def send_packet(values):
    send_i2c(BOSON_BUS, BOSON_I2C_ADDR, UART_REG, DISABLE)
    for val in values:
        send_i2c(BOSON_BUS, BOSON_I2C_ADDR, CMD_REG, val)
    send_i2c(BOSON_BUS, BOSON_I2C_ADDR, UART_REG, ENABLE)

def read_data():
    num = read_i2c(BOSON_BUS, BOSON_I2C_ADDR, BYTES_RDY_REG)
    data = [];
    for i in range(num):
        data.append(read_i2c(BOSON_BUS, BOSON_I2C_ADDR, CMD_REG))
    return data

def send_ffc():
    values = [0x8E, 0x00, 0x12, 0xC0, 0xFF, 0xEE, 0x00, 0x05, 0x00, 0x07, 
            0xFF, 0xFF, 0xFF, 0xFF, 0x6C, 0x5E, 0xAE]
    send_packet(values)

def get_SW_ver():
    values = [0x8E, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x05, 0x00, 0x22, 
            0xFF, 0xFF, 0xFF, 0xFF, 0x09, 0xBF, 0xAE]
    
    # flush and data waiting to be read before sending command
    read_data()
    
    # send commmand
    send_packet(values)
    
    # read response
    out = read_data()
    
    ver = [0, 0, 0]
    # parse response
    for i in range(3):
         digit = 0
         for j in range(len(out)-15+4*i,len(out)-11+4*i):
             digit = digit * 256 + out[j]
         ver[i] = digit
    print("SW Ver: " + str(ver[0]) + "." + str(ver[1]) + "." + str(ver[2]))


if __name__ == '__main__':
    send_ffc()
    get_SW_ver()

