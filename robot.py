from Raspi_MotorHAT import Raspi_MotorHAT

import atexit

class Robot:
    def __init__(self, motorhat_addr = 0x60):
        self.motorHat = Raspi_MotorHAT(addr = motorhat_addr)

        self.leftMotor = self.motorHat.getMotor(1)
        self.rightMotor = self.motorHat.getMotor(2)

        atexit.register(self.stop_motors)

    def convert_speed(self, speed):
        return (speed * 255) // 100

    def stop_motors(self):
        self.leftMotor.run(Raspi_MotorHAT.RELEASE)
        self.rightMotor.run(Raspi_MotorHAT.RELEASE)