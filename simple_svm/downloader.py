# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:18:43 2018

@author: kostis
"""

import youtube_dl
import pandas as pd
import youtube_dl
import shutil
import os
import sys



df=pd.read_csv('/home/kostis/Desktop/MultimodalAnalysis/test.csv')


for i in range(len(df)):
	if df['Label'][i]=='agreement':
		song=df['url'][i]
		os.system('youtube-dl --extract-audio --audio-format mp3 -o "/home/kostis/Desktop/MultimodalAnalysis/positive/simple_svm/%(title)s.%(ext)s" ' + song)


for i in range(len(df)):
	if df['Label'][i]=='disagreement':
		song=df['url'][i]
		os.system('youtube-dl --extract-audio --audio-format mp3 -o "/home/kostis/Desktop/MultimodalAnalysis/negative/simple_svm/%(title)s.%(ext)s" '+ song)
	
