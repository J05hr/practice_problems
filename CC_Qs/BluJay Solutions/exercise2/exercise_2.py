import time
"""
Continuing with your code with the Semi Truck, also implement a representation of an SUV that can:
1.   Move Forward
2.   Turn Right
3.   Turn Left
4.   Run Over Ford Pinto
Rules:
1.   If the SUV is already moving forward, the Move Forward command should generate an error
2.   The SUV can only turn left if the stop light's current signal is Left-Turn Green
3.   After each command to the SUV, the stop light's signal reverts back to Green
4.   The SUV can only Run Over Ford Pinto if its last action was to Move Forward
"""

# same assumptions as in part one
# we just need to abstract the semi methods into a Vehicle class
# semi and suv can both subclass from vehicle and we can just add the one unique method that SUV needs

# note that because the light resets after each action we block two vehicles from making a left at the same time
# we would need two independent left-green lights for them to proceed
# this seemed out of scope since we only have 2 vehicles but in reality we would make the vehicles actions async,
# implement the light reset in the light controller, and have it choose how long or how many cars to wait for.


class Vehicle:
    def __init__(self):
        # track current light signal
        self.stop_light = None
        # track if the vehicle is moving
        self.in_motion = False
        # track the last command, None, 1(forward), 2(right), 3(left), or 4(stop)
        self.last_command = None
        # as an add-on track the current direction
        self.current_direction = 0

    def read_signal(self, traffic_light):
        self.stop_light = traffic_light
        if self.stop_light.current_signal != 1:
            self.stop(self.stop_light.current_signal)

    def stop(self, signal):
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


class Semi(Vehicle):
    def __init__(self):
        super().__init__()


class SUV(Vehicle):
    def __init__(self):
        super().__init__()
        # track last action unique to suvs: 1(run over ford pinto), 2(waste gas), 3(take the kids to practice)
        self.last_suv_command = None

    def run_over_ford(self):
        if self.in_motion:
            self.last_suv_command = 1
        else:
            raise Exception("You can't run over anything if you're standing still")


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
        # create a suv
        self.suv = SUV()
        # create a traffic light
        self.tl = TrafficLight()
        # initialize the vehicles with the current light
        self.semi.read_signal(self.tl)
        self.suv.read_signal(self.tl)

    # command the traffic light and have it callback to the semi , 1(green), 2(yellow), 3(red), 4(left green)
    def tl_command(self, signal_code):
        self.tl.change_signal(signal_code)
        self.semi.read_signal(self.tl)
        self.suv.read_signal(self.tl)


if __name__ == '__main__':
    re = RoadEnv()
    # light starts green, tell the semi and suv to move forward
    re.semi.move_forward()
    re.suv.move_forward()
    # turn the light yellow then red, will callback and stop the vehicles
    re.tl_command(2)
    time.sleep(3)
    re.tl_command(3)
    # light will reset to green
    # turn the light left-green, vehicles will come to a stop on intermediate red, tell the vehicles to turn left
    re.tl_command(4)
    re.semi.turn_left()
    # need to turn the light left-green again for the suv since the light will reset after each vehicle
    re.tl_command(4)
    re.suv.turn_left()
    # vehicles makes the left-turn, light will reset to green, semi will continue forward
    # now tell the SUV to run over a ford pinta
    re.suv.run_over_ford()
    # suv complies happily but hopes the semi doesn't notice and get any ideas
