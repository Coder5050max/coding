import pandas as pd


df1=pd.read_excel('MarksTable.xlsx')
print(df1)

df2=pd.read_excel('NewStudent.xlsx')
print(df2)


print(df1.columns)
print(df2.columns)

df=pd.merge(df2,df1,on='Roll_Number',how='outer')
print(df)

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
print(df.head(5))