import cv2
import os
import json

import serial
import threading
import random
import time




BUFFER = ""
BOOL = True
# 读取接受的数据
def read_data(ser):
    global BUFFER, BOOL
    #while BOOL:
    #if ser.in_waiting:
    BUFFER = ser.read(ser.in_waiting)  # 接收数据默认为16进制
    try:
        BUFFER = BUFFER.decode("utf-8")  # 使用utf-8格式解码
    except:
        print("decode error")
    print("receive: ", BUFFER, "\n>>", end="")
    if BUFFER == "quit":
        print("oppo serial has closed.\n>>", end="")


def openPort(portx, bps, timeout):
    ret = False
    ser = serial.Serial()
    try:
        # open the serial port and get the serial port object
        ser = serial.Serial(portx, bps, timeout=timeout)
        if ser.is_open:
            ret = True
            #threading.Thread(target=read_data, args=(ser, )).start()
            #print("串口打开成功！")
        else:
            print("串口打开失败！")
            ser.close()
            
    except Exception as error:
        print("--serial port error--", error)
    return ser, ret


def closePort(ser):
    global BOOL
    BOOL = False
    ser.close()


def readPort():
    global BUFFER
    string = BUFFER
    BUFFER = ""
    return string


def writePort(ser, text):
    result = ser.write(text.encode('ascii'))
    return result

if __name__ == '__main__':


    while 1:
        # 设置电脑端口  不知道哪个是就用串口助手看一下
        ser, ret = openPort('COM1', 115200, 60)
        text = random.randrange(0, 100) % 4

        text = str(text)
        print(text)
        string = readPort()
        writePort(ser, text)
        read_data(ser)
        closePort(ser)



