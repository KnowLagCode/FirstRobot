import robot
from Raspi_MotorHAT import Raspi_MotorHAT
from time import sleep

zoomer = robot.Robot()
zoomer.leftMotor.setSpeed(150)
zoomer.rightMotor.setSpeed(150)
zoomer.leftMotor.run(Raspi_MotorHAT.FORWARD)
zoomer.rightMotor.run(Raspi_MotorHAT.FORWARD)
sleep(1)