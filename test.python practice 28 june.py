import pandas as pd

df=pd.read_csv('student_info.csv')
print(df.info())
print(df.describe)
print(df.describe())
print(df.head(5))
print(df.tail(5))
print(df.T)
print(df.columns)
print(df[1:4])
print(df[1:6])
df.pop('Course')

df1 = pd.DataFrame({'Student_Name':['Sairaj Bahirat','Parin Vanjari','Nishan Deshmukh','Kirti Singh','Om Shinde'],
                    'Student_ID' :[234568,234568,1235789,909087,456732],
                    'Roll_No':[18,23,55,66,60],
                    'Marks':[70,0,'AB',85,90]},
                    index=[1,2,3,4,5])
print(df1)

df2 = pd.DataFrame({'Student_Name':['Soham Khare','Ishan Reddy','Arvind Swamy','Rohan Joshi','Pratik Sawant'],
                    'Student_ID' :[9012,8091,7050,5050,2525],
                    'Roll_No':[70,35,50,85,7],
                    'Marks':[70,0,0,'AB','AB']},
                    index=[6,7,8,9,10])
print(df2)

result=pd.concat([df1,df2])
print(result)
merge_df=pd.merge(df1,df2,on='Marks',how='inner')
print(merge_df)
merge_df=pd.merge(df1,df2,on='Marks',how='left')
print(merge_df)
merge_df=pd.merge(df1,df2,on='Marks',how='right')
print(merge_df)     








