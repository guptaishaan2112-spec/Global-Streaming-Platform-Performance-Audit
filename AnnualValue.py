from creating_data import df
import numpy as np
#method 1
def annual_value_calc():
    l=[]
    x=0
    for i in df['Tier']:
        j=df['MonthsActive'][x]
        if i=='Basic':
            value=9.99*j
            l.append(value)
        elif i=='Standard':
            value=14.99*j
            l.append(value)
        elif i=='Premium':
            value=19.99*j
            l.append(value)
        else:
            value=0
            l.append(value)
        x+=1
    return np.array(l)

print(annual_value_calc())
df['TotalRevenue']=annual_value_calc()
df.to_csv('dataframe.csv',index=False)


        
