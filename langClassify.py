from google.colab import files

import pandas as pd
import re
from langdetect import detect



df = pd.read_csv('train.csv')
print(df.tail())

messages = [(df['comment_text'][i]) for i in range(159570) ]

df['lang'] = 'Nan'
for i in range(50000):
    messages[i]=re.sub('[^A-Za-z]+', ' ', messages[i])
    messages[i] = messages[i][0:35]
    try:
      x = detect(messages[i]) 
      df['lang'][i] = x
      print(i,' ',x)
    except Exception as e:
      df['lang'][i] = 'NaN'
      print(e)
for i in range(50000,100000):
    messages[i]=re.sub('[^A-Za-z]+', ' ', messages[i])
    messages[i] = messages[i][0:35]
    try:
      x = detect(messages[i]) 
      df['lang'][i] = x
      print(i,' ',x)
    except Exception as e:
      df['lang'][i] = 'NaN'
      print(e)
for i in range(100000,159570):
    messages[i]=re.sub('[^A-Za-z]+', ' ', messages[i])
    messages[i] = messages[i][0:35]
    try:
      x = detect(messages[i]) 
      df['lang'][i] = x
      print(i,' ',x)
    except Exception as e:
      df['lang'][i] = 'NaN'
      print(e)

df1 = df[:50000]
df1.to_csv('Dataset11.csv',index=False)
df2 = df[50000:100000]
df2.to_csv('Dataset22.csv',index=False)
df3 = df[100000:159570]
df3.to_csv('Dataset33.csv',index=False)


