from robot import Robot
from time import sleep

class ObstacleAvoidingBehavior:
    def __init__(self, the_robot):
        self.robot = the_robot
        self.speed = 60

    def get_speeds(self, nearest_distance):
        if nearest_distance >= 1.0:
            nearest_speed = self.speed
            furthest_speed = self.speed
            delay = 100
        elif nearest_distance > 0.5:
            nearest_speed = self.speed
            furthest_speed = self.speed * 0.8
            delay = 100
        elif nearest_distance > 0.2:
            nearest_speed = self.speed
            furthest_speed = self.speed * 0.6
            delay = 100
        elif nearest_distance > 0.1:
            nearest_speed = -self.speed * 0.4
            furthest_speed = -self.speed
            delay = 100
        else:
            nearest_speed = -self.speed
            furthest_speed = -self.speed
            delay = 250
        return nearest_speed, furthest_speed, delay
  
    def run(self):
        while True:
            left_distance = self.robot.left_distance_sensor.distance
            right_distance = self.robot.right_distance_sensor.distance

            print("Left: {l:.2f}, Right: {r:.2f}".format(l = left_distance, r = right_distance))

            nearest_speed, furthest_speed, delay = self.get_speeds(min(left_distance, right_distance))

            print(f"Distances: l {left_distance:.2f}, r {right_distance:.2f}. Speeds: n: {nearest_speed}, f: {furthest_speed}. Delay: {delay}")

            if left_distance < right_distance:
                self.robot.set_left(nearest_speed)
                self.robot.set_right(furthest_speed)
            else:
                self.robot.set_right(nearest_speed)
                self.robot.set_left(furthest_speed)

            sleep(delay * 0.001)

if __name__ == "__main__":
    bot = Robot()
    behavior = ObstacleAvoidingBehavior(bot)
    behavior.run()