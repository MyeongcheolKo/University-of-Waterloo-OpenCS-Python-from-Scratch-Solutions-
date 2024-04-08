from math import pi
volume = pi * pow(8 / 2,2) * 27
straw_jam = 8 * 1000
print(int(straw_jam / volume + 0.5))
'''Alternative using ceil
from math import pi
from math import ceil
volume = pi * pow(8 / 2,2) * 27
straw_jam = 8 * 1000
print(ceil(straw_jam / volume))
'''
