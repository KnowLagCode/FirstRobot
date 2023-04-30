from Raspi_MotorHAT import Raspi_MotorHAT

import atexit

class Robot:
    def __init__(self, motorhat_addr = 0x60):
        self.motorHat = Raspi_MotorHAT(addr = motorhat_addr)

        self.leftMotor = self.motorHat.getMotor(1)
        self.rightMotor = self.motorHat.getMotor(2)

        atexit.register(self.stop_motors)

    def convert_speed(self, speed):
        mode = Raspi_MotorHAT.RELEASE
        if speed > 0:
            mode = Raspi_MotorHAT.FORWARD
        elif speed < 0:
            mode = Raspi_MotorHAT.BACKWARD

        output_speed = (abs(speed) * 255) // 100
        return mode, int(output_speed)
    
    def set_left(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.leftMotor.setSpeed(output_speed)
        self.leftMotor.run(mode)

    def set_right(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.rightMotor.setSpeed(output_speed)
        self.rightMotor.run(mode)

    def stop_motors(self):
        self.leftMotor.run(Raspi_MotorHAT.RELEASE)
        self.rightMotor.run(Raspi_MotorHAT.RELEASE)