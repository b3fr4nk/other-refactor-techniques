# Kami Bigdely
# Move Field

class Car:
    """represents a car"""

    def __init__(self, engine, wheels, cabin, fuel_tank):
        self.engine = engine
        self.wheels = wheels
        # Set wheels' car reference into each wheel.
        for w in wheels:
            w.set_car(self)

        self.cabin = cabin
        self.fuel_tank = fuel_tank


class Wheel:
    """Represents a wheel"""
    # TODO: You may add tpms as a method parameter here to
    #       initilaize the 'Wheel' object or you can create
    #       a setter method to set the tpms of the wheel. (you can do
    #       both of course.)

    def __init__(self, car=None, tpms_sensor=None, wheel_location=None):
        self.car = car
        self.tpms_sensor = tpms_sensor
        self.wheel_location = wheel_location

    def install_tire(self):
        """Print the steps to replace a tire"""
        print('remove old tube.')
        # TODO: Rewrite the following after moving tpms to the 'Wheel' class
        print('cleaned tpms: ',
              self.car.tpms_di[self.wheel_location].get_serial_number,
              '.')
        print('installed new tube.')

    def read_tire_pressure(self):
        """Returns the status of the tpms sensor"""
        return self.tpms_sensor.get_pressure()

    def set_car(self, car):
        """assigns the wheel to a car"""
        self.car = car


class Tpms:
    """Tire Pressure Monitoring System.
    """

    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.sensor_transmit_range = 300  # [feet]
        self.sensor_pressure_range = (8, 300)  # [PSI]
        self.battery_life = 6  # [year]

    def get_pressure(self):
        """Return tire pressure"""
        return 3

    def get_serial_number(self):
        """Return serial number"""
        return self.serial_number


class Engine:
    def __init__(self):
        pass


class FuelTank:
    def __init__(self):
        pass


class Cabin:
    def __init__(self):
        pass


engine = Engine()

# TODO: Rewrite the following after moving tpms to the 'Wheel' class.
wheels = [Wheel(None, Tpms(983408543), 'front-right'), Wheel(None, Tpms(4343083), 'front-left'),
          Wheel(None, Tpms(23654835), 'back-right'), Wheel(None, Tpms(3498857), 'back-left')]

cabin = Cabin()

fuel_tank = FuelTank()

my_car = Car(engine, wheels, cabin, fuel_tank)
