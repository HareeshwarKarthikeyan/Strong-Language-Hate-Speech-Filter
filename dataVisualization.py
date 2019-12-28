# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 05:37:08 2019

@author: Akshit
"""

'toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'

import pandas as pd

df = pd.read_csv('data_train_clean.csv')

df.drop(['id'], axis=1, inplace=True)

toxic = df[df.toxic==1]
toxic.drop(['severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate'], axis=1, inplace=True)
print(len(toxic))
toxic.to_csv('toxic.csv', index=False)

severe_toxic = df[df.severe_toxic==1]
severe_toxic.drop(['toxic', 'obscene', 'threat', 'insult', 'identity_hate'], axis=1, inplace=True)
print(len(severe_toxic))
severe_toxic.to_csv('severe_toxic.csv', index=False)

obscene = df[df.obscene==1]
obscene.drop(['toxic', 'severe_toxic', 'threat', 'insult', 'identity_hate'], axis=1, inplace=True)
print(len(obscene))
obscene.to_csv('obscene.csv', index=False)

threat = df[df.threat==1]
threat.drop(['toxic', 'severe_toxic', 'obscene', 'insult', 'identity_hate'], axis=1, inplace=True)
print(len(threat))
threat.to_csv('threat.csv', index=False)

insult = df[df.insult==1]
insult.drop(['toxic', 'severe_toxic', 'obscene', 'threat', 'identity_hate'], axis=1, inplace=True)
print(len(insult))
insult.to_csv('insult.csv', index=False)

identity_hate = df[df.identity_hate==1]
identity_hate.drop(['toxic', 'severe_toxic', 'obscene', 'threat', 'insult'], axis=1, inplace=True)
print(len(identity_hate))
identity_hate.to_csv('identity_hate.csv', index=False)



import matplotlib.pyplot as plt
fig = plt.figure()

x = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
height=[len(toxic), len(severe_toxic), len(obscene), len(threat), len(insult), len(identity_hate)]
plt.bar(x, height, width=0.8)
plt.show()



