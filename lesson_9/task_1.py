import time


class TrafficLight:
    __color = {'red': 8, 'yellow': 3, 'green': 7}

    @staticmethod
    def running():
        for color, seconds in TrafficLight.__color.items():
            if color == 'red':
                print(f"\033[31m{color}")
            elif color == 'yellow':
                print(f"\033[33m{color}")
            elif color == 'green':
                print(f"\033[32m{color}")

            time.sleep(seconds)


traffic = TrafficLight()
traffic.running()
