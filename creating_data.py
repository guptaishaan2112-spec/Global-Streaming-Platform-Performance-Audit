import numpy as np
import pandas as pd
np.random.seed(42)
dataset={
    'UserID':np.arange(10001,15001),
    'Tier':np.random.choice(['Basic','Standard','Premium'],size=5000),
    'MonthsActive':np.random.randint(1,13,size=5000),
    'HoursStreamed':np.random.normal(250,75,5000),
    'Region':np.random.choice(['North America','Europe','Asia','Latin America'],size=5000)
}

df=pd.DataFrame(dataset)
df['Price']=df['Tier'].map({
    'Basic':9.99,
    'Standard':14.99,
    'Premium':19.99
})
df.to_csv('dataframe.csv',index=False)
#print(df)