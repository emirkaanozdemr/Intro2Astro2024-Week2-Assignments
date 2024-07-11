## Problem: Calculate the gravitational force between a 3 solar mass star and its 10 Jupiter mass planet 2 au away.

import astropy.units as u
import astropy.constants as c

sun=c.M_sun
star=sun*3
jupyter=c.M_jup
planet=jupyter*10
distance = 2 * u.au


force=(u.G)*star*planet/distance**2

force_in_newtons=force.to(u.N)
print(force_in_newtons)
