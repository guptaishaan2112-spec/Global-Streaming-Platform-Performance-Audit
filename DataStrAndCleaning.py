from creating_data import df
import AnnualValue
import numpy as np
np.random.seed(0)
#5% of total values=250
random_rows = np.random.choice(df.index, size=250, replace=False)
df.loc[random_rows, 'HoursStreamed'] = np.nan
median=df['HoursStreamed'].median()
df=df.fillna({'HoursStreamed':median})
df1=df.loc[(df['HoursStreamed']>450) | (df['HoursStreamed']<50)]
df1.to_csv('extremeORlessUser.csv',index=False)
df2=df.loc[(df['HoursStreamed']>450)]
df2.to_csv('extremeUser.csv',index=False)
df3=df.groupby('Region')['TotalRevenue'].sum()
df4=df.groupby('Region')['MonthsActive'].mean()
print(df3)
print(df4)
df['Engagement_tier']=''
df.loc[(df['HoursStreamed']>350),'Engagement_tier']='High Engagement'
df.loc[(df['HoursStreamed']<=350)&(df['HoursStreamed']>=150),'Engagement_tier']='Medium Engagement'
df.loc[(df['HoursStreamed']<150),'Engagement_tier']='Low Engagement'
df.to_csv('dataframe.csv',index=False)
df5=df.loc[(df['Engagement_tier']=='High Engagement') & (df['MonthsActive']<6)]
df5.to_csv('Higheng6M.csv',index=False)