# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 12:26:36 2021

@author: hp
"""
ansr='pink'
rep=""
trie=3
i=0
lose=False

while ansr!=rep and not lose:
    if trie>i:
        rep=input('what\'s my fav color :')
        trie-=1
    else:
        lose=True

if lose :
  print('you lose sorry for you')
else:
  print('congrat !! you win  ')       