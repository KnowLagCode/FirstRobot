from Raspi_MotorHAT import Raspi_MotorHAT

import time
import atexit

motorHat = Raspi_MotorHAT(addr=0x60)
leftMotor = motorHat.getMotor(1)
rightMotor = motorHat.getMotor(2)

def turn_off_motors():
    leftMotor.run(Raspi_MotorHAT.RELEASE)
    rightMotor.run(Raspi_MotorHAT.RELEASE)

atexit.register(turn_off_motors)

leftMotor.setSpeed(150)
rightMotor.setSpeed(150)

leftMotor.run(Raspi_MotorHAT.FORWARD)
rightMotor.run(Raspi_MotorHAT.FORWARD)
time.sleep(1)