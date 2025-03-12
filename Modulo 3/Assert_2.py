from types import *
#import pandas as pd

#----------------8. declaracion de afirmación any()----------
#------------------------------------------------------------
example = [5,3,1,6,6]   #true
booleans = [False, False,True, False] #true

assert any(example) == True # Success Example
assert any(booleans) == True # Success Example


#-------------9. declaracion de afirmación all()-------------
#------------------------------------------------------------
all(example) #true
all(booleans)  #false

assert all(example) # Success Example
#assert all(booleans) # Fail Example


#------------10. Objetos personalizados-----------------------
#------------------------------------------------------------
'''  
type(object).__name__
df = pd.DataFrame()

type(df).__name__ == 'DataFrame' # True Boolean
type(df).__name__ == 'DataFrame' # True Boolean
type(df).__name__ == type([]).__name__ #False Boolean
type(df).__name__ is type([]).__name__ #False Boolean

assert(type(df).__name__ == 'DataFrame')# Success Example
#assert(type(df).__name__ ==type([]).__name__) # Fail Example
'''