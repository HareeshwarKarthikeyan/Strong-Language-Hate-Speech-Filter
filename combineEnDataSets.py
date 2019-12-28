import pandas as pd




df1 = pd.read_csv('Dataset11.csv')
df2 = pd.read_csv('Dataset22.csv')
df3 = pd.read_csv('Dataset33.csv')


df = df1.append(df2)
df = df.append(df3)

print(df.describe())


df.to_csv('Dataset02en.csv',index=False)
     