'''
                       DATA ANALYSIS
                       --------------
    -->THIS is the process of inspecting,cleaning,transforming and modeling data to discover useful insights...

    types of DA:
    1.descriptive analysis
      -->summarizing data
      
    2.diagnostic analysis
      -->understanding causes
      
    3.predictive analysis
      -->forecasting future outcomes
      
    4.prescriptive analysis
      -->suggesting actions based on data


    ->why DA?
     1.to improve decision making
     2.detects trends and pattern

     ------NUMPY-------
     (NUMERICAL PYTHON)
     
     -->this python library for numerical computing.it support for multi-dimensional arrays and linear algebra operations,
     making it essential for data analysis...

      -> using numpy id DA:
      1.improve performance
      2.simplifies complex operations
      3.easy data manipulation

#1d array
import numpy as np
arr_=np.array([1,2,3,4])
print(arr_)


#2d array
import numpy as np
arr=np.array([[4,5,6,7],[1,2,3,4]])
print(arr)

#3d array
import numpy as np
arr=np.array([[4,5,6,7],[1,2,3,4],[9,8,4,5]])
print(arr)


#to find the dimension of array (m x n)
import numpy as np
arr=np.array([[1,2,3,4],[1,2,3,4]])
print(arr)
print(arr.shape)

#to change (m x n) to (n x m)
import numpy as np
arr=np.array([[1,2,3,4],[1,2,3,4]])
print(arr)
print(arr.shape)
reshaped=arr.reshape(4,2)
print(reshaped)



import numpy as np
arr_=np.array([1,2,3,4])
print(arr_)
print(arr_*2)



import numpy as np
arr1=np.array([[1,2],[1,2]])
arr2=np.array([[3,2],[1,4]])
print(np.dot(arr1,arr2))



#shallow copy******

import numpy as np
arr1=np.array([10,20,30])
n_copy=arr1.view()
arr1[0]=100
print(n_copy)
print(arr1)

#deep copy********

d_copy=arr1.copy()
arr1[1]=100
print(d_copy)
print(arr1)

    ------PANDAS-----
    ->pandas is a powerful data maipulation and analysis library
    ->it provides data structure like series and dataframe for effecient data handling

methods(in Series):
mean()
sum()
max()
min()
apply()
map()


import pandas as pd
any=pd.Series([2999,15999,52999,4999,1999],index=['earbuds','smartphone','laptop','watch','footwear'])
print(any)


dataframe

'''
import pandas as pd
data={'product':['earbuds','smartphone','laptop','watch','footwear'],'brand':['noise','oneplus','HP','bolt','puma'],'price':[2999,15999,52999,4999,1999],
      'stock':[50,15,25,30,70]}
dip=pd.DataFrame(data)
print(dip)

