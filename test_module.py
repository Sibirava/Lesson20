# 1)
import some_module

#2)
from some_module import __a, __b, A, B

a = A()

# 3)
from some_module import __a as alfa

a = alfa

#4)
from some_module import *
from some2 import *
from some1 import *

print(test_a())  # вызывает ближайшую доступную
