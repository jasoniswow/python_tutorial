# This is an example for constructing class, attribute and method


class Planet:

    # initialize the attributes for instance, "self" is always needed
    def __init__(self,name,radius,gravity,system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system


    # attribute for class
    shape = 'round'


    # object method
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'


    # decorater and class method
    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity.'


    # decorater and static method
    # static method can only access the parameters passing to it
    # you can set default values for method parameters
    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'The planet spins at {speed}'


