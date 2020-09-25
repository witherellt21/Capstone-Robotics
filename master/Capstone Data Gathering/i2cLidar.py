'''
Author: Taylor Witherell
File: i2cLidar.py
Description: Uses I2C communications protocol to get data from the lidar sensor
Pin outs: 5V, GND, SCL (column 1, row 3), SDA (column 1, row 4)
'''

from smbus2 import SMBus, i2c_msg
#from smbus import *

i2c_bus = SMBus(1)

i2c_address = '/dev/i2c-1'

open(i2c_address) # To open a given i2c bus.

i2c_addr = '0x10'
register = '0x2C'

i2c_bus.read_byte_data(i2c_addr,register,force=None) # To read a single byte from a designated register.
#read_block_data(i2c_addr,register,force=None) # To read a block of up to 32-bytes from a given register.
#read_i2c_block_data(i2c_addr,register,length,force=None) # To read a block of byte data from a given register.
#read_word_data(i2c_addr,register,force=None) # To read a single word (2 bytes) from a given register.

close() # To close I2C connection.