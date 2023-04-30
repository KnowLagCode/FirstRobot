import robot
from Raspi_MotorHAT import Raspi_MotorHAT
from time import sleep

zoomer = robot.Robot()
zoomer.leftMotor.setSpeed(zoomer.convert_speed(80))
zoomer.rightMotor.setSpeed(zoomer.convert_speed(80))
zoomer.leftMotor.run(Raspi_MotorHAT.FORWARD)
zoomer.rightMotor.run(Raspi_MotorHAT.FORWARD)
sleep(1)