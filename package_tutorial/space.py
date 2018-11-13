from space.planet import Planet
from space.calc import planet_mass,planet_vol


# create an instance of class "Planet"
naboo = Planet('Naboo', 300000, 8, 'Naboo System')


# print out
print (f'Name: {naboo.name}')
print (naboo.spin('1000 miles per second'))


# calculation
naboo_mass = planet_mass(naboo.gravity,naboo.radius)
naboo_vol = planet_vol(naboo.radius)
print (f'{naboo.name} has a mass of {naboo_mass} and a volumn of {naboo_vol}')
