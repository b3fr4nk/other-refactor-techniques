# by Kami Bigdely
# Replace magic numbers with named constanst


class ElectricForce:
    """Represents an electric force between two charges"""
    COULOMB_CONST = 8.9875517923*1e9

    def __init__(self):
        self.get_input()

    def get_input(self):
        """Gets user input through the terminal and assigns local variables"""
        self.q1 = int(input('Enter a value of charge q1: '))
        self.q2 = int(input('Enter a value of charge q2: '))
        self.distance = int(
            input("Enter the distance between two charges: "))

    def get_electrical_force(self):
        """returns a the force in newtons as a number"""
        return self.COULOMB_CONST * self.q1 * self.q2/(self.distance**2)

    def __repr__(self):
        # return "Electric Force between q1 and q2 is: ", self.get_electrical_force(), "Newton"
        return f'Electric Force between q1 and q2 is: {self.get_electrical_force()} Newtons'


# First Section
# Given two point charges, calcualte the electric force exerted on them.

force = ElectricForce()
print(force)

# Second Section


def is_even(num):
    """Returns a string denoting whether a number is even or odd"""
    if num % 2 == 0:
        return 'is an even number'
    return 'is an odd number'


num = int(input('Enter an integer number: '))
print(is_even(num))
