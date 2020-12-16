import time
"""
Implement a representation of an Eighteen Wheeler (Semi Truck).
The Semi should be able to do the following on command:
  1.   Move Forward
  2.   Turn Right
  3.   Turn Left
  4.   Jack Knife to a Stop
Additionally, create a Traffic Control Device -specifically, a stop light.
Given the appropriate command, this stop light has each of the following signals:
  1.   Green
  2.   Yellow
  3.   Red
  4.   Left-Turn Green
Rules:
  1.   If the Semi is already moving forward, the Move Forward command should generate an error
  2.   Only one signal in the traffic light can be on at a given time
  3.   The Semi can only turn left if the stop light's current signal is Left-Turn Green
  4.   After jack knifing to a stop, the Semi can only Move Forward
  5.   After each command to the Semi, the stop light's signal reverts back to Green
"""

# assuming we can stop the semi on any signal if we choose,
# assuming the semi has to choose to move forward after a stop
# assuming the semi will continue to move forward after turns until it is told to stop or the light forces a stop
# assuming semi will start stopping on a yellow light
# assuming the lights follow a logical progression and aren't arbitrary
# i.e. there is an assumed red light between a green and a left-green, yellow can't come after red


class Semi:
    def __init__(self):
        # track current light signal
        self.stop_light = None
        # track if the semi is moving
        self.in_motion = False
        # track the last command, None, 1(forward), 2(right), 3(left), or 4(stop)
        self.last_command = None
        # as an add-on track the current direction
        self.current_direction = 0

    def read_signal(self, traffic_light):
        self.stop_light = traffic_light
        if self.stop_light.current_signal != 1:
            self.jk_to_stop(self.stop_light.current_signal)

    def jk_to_stop(self, signal):
        # assuming we can choose to stop on any signal and at any time
        self.in_motion = False
        self.last_command = 4
        if signal != 4:
            self.stop_light.change_signal(1)

    def turn_left(self):
        # can't turn left without a left arrow
        if self.stop_light.current_signal != 4:
            raise Exception("Can't turn left on this signal")
        self.current_direction -= 90
        if self.current_direction == -90:
            self.current_direction = 270
        self.last_command = 3
        self.stop_light.change_signal(1)
        self.move_forward()

    def turn_right(self):
        # can't turn right without a green signal
        if self.stop_light.current_signal != 1:
            raise Exception("Can't turn right on this signal")
        self.current_direction += 90
        if self.current_direction == 360:
            self.current_direction = 0
        self.last_command = 2
        self.in_motion = False
        self.move_forward()

    def move_forward(self):
        # cant move forward twice, raise an exception
        if self.in_motion:
            raise Exception("Semi is already in motion")
        # can't move forward without a green signal
        if self.stop_light.current_signal != 1:
            raise Exception("Can't move forward on this signal")
        self.in_motion = True
        self.last_command = 1


class TrafficLight:
    def __init__(self):
        # track a current signal, 1(green), 2(yellow), 3(red), 4(left green),
        self.current_signal = 1

    def change_signal(self, new_signal_code):
        self.current_signal = new_signal_code


class RoadEnv:
    def __init__(self):
        # create a semi
        self.semi = Semi()
        # create a traffic light
        self.tl = TrafficLight()
        # initialize the semi with the current light
        self.semi.read_signal(self.tl)

    # command the traffic light and have it callback to the semi , 1(green), 2(yellow), 3(red), 4(left green)
    def tl_command(self, signal_code):
        self.tl.change_signal(signal_code)
        self.semi.read_signal(self.tl)


if __name__ == '__main__':
    try:
        re = RoadEnv()
        print("inMotion: " + str(re.semi.in_motion) + ", last command: " + str(re.semi.last_command) + ", direction: " + str(re.semi.current_direction))
        # light starts green, tell the semi to move forward
        re.semi.move_forward()
        print("inMotion: " + str(re.semi.in_motion) + ", last command: " + str(re.semi.last_command) + ", direction: " + str(re.semi.current_direction))
        # turn the light yellow then red, will callback and stop the semi
        re.tl_command(2)
        time.sleep(3)
        re.tl_command(3)
        print("inMotion: " + str(re.semi.in_motion) + ", last command: " + str(re.semi.last_command) + ", direction: " + str(re.semi.current_direction))
        # light will reset to green
        # turn the light left-green, semi will come to a stop on intermediate red, then tell the semi to turn left
        re.tl_command(4)
        re.semi.turn_left()
        print("inMotion: " + str(re.semi.in_motion) + ", last command: " + str(re.semi.last_command) + ", direction: " + str(re.semi.current_direction))
        # semi makes the left-turn, light will reset to green, semi will continue forward
        # now tell the semi to turn right
        re.semi.turn_right()
        print("inMotion: " + str(re.semi.in_motion) + ", last command: " + str(re.semi.last_command) + ", direction: " + str(re.semi.current_direction))
        # semi will turn right and continue forward
        # light is still green, now tell it to turn left to test the exception
        re.semi.turn_left()
    except Exception as e:
        print(e)








