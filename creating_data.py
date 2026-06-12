import numpy as np
import pandas as pd
np.random.seed(42)
dataset={
    'UserID':np.arange(10001,15001),
    'Tier':np.random.choice(['Basic','Standard','Premium'],size=5000),
    'MonthsActive':np.random.randint(1,13,size=5000),
    'HoursStreamed':np.random.normal(250,75,5000)
}
df=pd.DataFrame(dataset)
print(df)