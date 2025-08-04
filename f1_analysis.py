import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('C:\VsCode\F1_Projects\\1_results_2025.csv')

#Checking what is inside of the dataframe
print(df.columns)

#podiums = pd.concat([df['P1'], df['P2'], df['P3']])
#counts =  podiums.value_counts()
#result = counts.reset_index()
#result.columns= ['Teams','Podiums']
                
df.plot(
    x='Team',
    y=['Winner', 'Team_p2', 'Team_p3'],
    kind='bar',
    title='Total Podiums by Team',
    xlabel='Team',
    ylabel='Number of Podiums'
)
plt.show()

