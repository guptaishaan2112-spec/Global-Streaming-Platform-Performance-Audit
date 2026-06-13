import matplotlib.pyplot as plt
from DataStrAndCleaning import df 
from DataStrAndCleaning import df3
df3=df3.sort_values(ascending=False)
print(df3)
fig, axes=plt.subplots(3,1,figsize=(10,8))

df3.plot(kind='bar',color=['blue','green','magenta','orange'],alpha=0.6,edgecolor='black',linewidth=1.2,ax=axes[0])
axes[0].set_xlabel('Region')
axes[0].set_ylabel('Tota Revenue')
axes[0].set_title('The Revenue Story')
axes[0].grid(True,alpha=0.3,axis='y')

df.plot(kind='hist',x='HoursStreamed',bins=30,color='pink',edgecolor='black',ax=axes[1],alpha=0.6)
axes[1].set_xlabel('Hours Streamed')
axes[1].set_ylabel('Number of Users')
axes[1].set_title('The Engagement distribution')
axes[1].grid(True,alpha=0.3,axis='y')

df.plot(kind='scatter',x='HoursStreamed',y='TotalRevenue',color='lightblue',ax=axes[2])
axes[2].set_xlabel('Hours Streamed')
axes[2].set_ylabel('Total Revenue')
axes[2].set_title('The Engagement vs Revenue Link')
axes[2].grid(True,alpha=0.3)

plt.tight_layout()
plt.show()