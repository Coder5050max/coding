import pandas as pd
import numpy as np

df = pd.read_csv('Football_teams_price_data.csv')

# Prints top 10 records 
print(df.head(10))
# Prints 10 records starting from bottom to up
print(df.tail(10))
# Gives info about dataframe(df)
print(df.info)
# describes the statistical information about the numerical column 
print(df.describe())
# Displays column names of the datasets 
print(df.columns)
# Rows becomes column and vica versa
print(df.T)
# Sorts the data in ascending order 
print(df.sort_values('AveragePlayerAge'))
# Sorts the data in descending order
print(df.sort_values('AveragePlayerAge', ascending = False))
print(df.sort_values('TotalGoalsLastSeason', ascending = False))
# Accesing particularly required rows 
print(df[10:20])
print(df[4990:4999])
# Displaying records of players having goals less than 30
goals_30=df[df.TotalGoalsLastSeason<30]
print(df[df.TotalGoalsLastSeason<30])
# Tells us the quantity of records of goals scored less than 30 
print (len(goals_30))
# Deleting MatcHWonLastSeason column
new_df=df.pop('MatchesWonLastSeason')
print(new_df)
print(df.head(5))
# using apply in pandas 
print(df['MatchesDrawnLastSeason'].apply(np.square))
print(df['TotalGoalsLastSeason'].apply(np.sqrt))
df['SquareRootOfTotalGoalsLastSeason']=df['TotalGoalsLastSeason'].apply(np.sqrt)
print(df['SquareRootOfTotalGoalsLastSeason'])



df1=pd.DataFrame({ 'A': ['A1', 'B1', 'C1','D1'],
                   'B': ['A2', 'B2', 'C2','D2'],
                   'C': ['A3', 'B3', 'C3','D3'],
                   'D': ['A4', 'B4', 'C4','D4']},
                   index=[0,1,2,3])  
  

df2 = pd.DataFrame({ 'E':['A4', 'B4', 'C0', 'D4'],
                     'F':['A5', 'B5', 'C3', 'D5'],
                     'C':['A6', 'C6', 'C6', 'D6'],
                     'G':['A7', 'B7', 'C7', 'D7']},
                     index=[0,1,2,3])
# concat or merging df1 and df2
result=pd.concat([df1,df2])
print(result)
merge_df=pd.merge(df1,df2, on='C',how='inner')

# loc and ilock 
s=pd.Series(list("abcdef"),index=[1,2,3,4,5,6])
print(s)
print(s.loc[4])
print(s.iloc[0])
print(s.iloc[0:2])
print(s.iloc[0:4])

new_s=s.sort_index()
print(new_s)
print(new_s.loc[4])
print(new_s.loc[4])













      


