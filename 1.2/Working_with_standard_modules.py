# import math
  
# for name in dir(math):
#   print(name, end="∖t")

# import math
# dir(math)

# from math import pi, radians, degrees, sin, cos, tan, asin

# ad = 90
# ar = radians(ad)
# ad = degrees(ar)

# print(ad == 90.)
# print(ar == pi / 2.)
# print(sin(ar) / cos(ar) == tan(ar))
# print(asin(sin(ar)) == ar)

# from math import e, exp, log

# print(pow(e, 1) == exp(log(e)))
# print(pow(2, 2) == exp(2 * log(2)))
# print(log(e, e) == exp(0))

# from math import ceil, floor, trunc

# x = 1.4
# y = 2.6

# print(floor(x), floor(y))
# print(floor(-x), floor(-y))
# print(ceil(x), ceil(y))
# print(ceil(-x), ceil(-y))
# print(trunc(x), trunc(y))
# print(trunc(-x), trunc(-y))

# from random import random

# for i in range(5):
#     print(random())

# from random import random, seed

# seed(0)

# for i in range(5):
#     print(random())

# from random import randrange, randint

# print(randrange(1), end=' ')
# print(randrange(0, 1), end=' ')
# print(randrange(0, 1, 1), end=' ')
# print(randint(0, 1))

# from random import randint

# for i in range(10):
#     print(randint(1, 10), end=',')

# from random import choice, sample

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(choice(my_list))
# print(sample(my_list, 5))
# print(sample(my_list, 10))

# from platform import platform

# print(platform())
# print(platform(1))
# print(platform(0, 1))

# from platform import processor

# print(processor())

# from platform import python_implementation, python_version_tuple

# print(python_implementation())

# for atr in python_version_tuple():
#     print(atr)

import math
print(result = math.e == math.exp(1))