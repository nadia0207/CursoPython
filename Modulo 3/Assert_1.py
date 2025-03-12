# Module Imports
from types import *
#import pandas as pd
#import numpy as np
from collections.abc import Iterable

#-----------------1. Igual o no igual a [valor]-------------

assert 5 == 5 # Success Example
#assert 5 == 3 # Fail Example


#-----------------2. type() is [valor]----------------------
assert type(5) is int # Success Example
#assert type(5) is not int # Fail Example

#----------------3. isinstance------------------------------
assert type(5) is int # Success Example
#assert type(5) is not int # Fail Example

#---------------4. is [Tipo booleano] ----------------------
true = 5==5
assert true is True # Success Example
#assert true is False # Fail Example

#-------------5. in y not in [iterable]----------------------
list_one=[1,3,5,6]
assert 5 in list_one # Success Example
#assert 5 not in list_one # Fail Example

#------------6. Mayor o menor que [valor]--------------------
assert 5 > 4 # Success Example
#assert 5 > 7 # Fail Example

#----------7. El módulo % es igual a [valor]-----------------
assert 2 % 2 == 0 # Success Example
#assert 2 % 2 == 1 # Fail Example

