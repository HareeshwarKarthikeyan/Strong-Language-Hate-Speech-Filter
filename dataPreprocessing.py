# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 07:37:58 2019

@author: Akshit
"""

import string
import pandas as pd

df = pd.read_csv('enDataset.csv')

def remove_punctuation(s):
    s = ''.join([i for i in s if i not in frozenset(string.punctuation+"0123456789")])
    return s.lower()

df['comment_text'] = df['comment_text'].apply(remove_punctuation)
#print(df['comment_text'])

df.to_csv('removedSpecialChar.csv' ,index=False)
