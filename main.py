import numpy as np
import pandas as pd
list=[1,1,3,7,2,4]
np_list=np.array(list)
print(np_list)
np_list=np_list+5
print(np_list)

data=pd.read_csv("csv/input.csv")
print(data)
