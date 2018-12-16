import numpy as np
import pandas as pd
# before importing matplotlib do the following when not having a window to open
# https://matplotlib.org/faq/howto_faq.html#generate-images-without-having-a-window-appear 
import matplotlib
matplotlib.use('SVG')
# End of import w/o window pop up

import matplotlib.pyplot as plt


#list=[1,1,3,7,2,4]
#np_list=np.array(list)
#print(np_list)
#np_list=np_list+5
#print(np_list)

#data=pd.read_csv("csv/input.csv")
#print(data)
#print(data[["Typ1"]])


year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
# Do not use  plt.show(), instead save figure
plt.savefig('myfig')

