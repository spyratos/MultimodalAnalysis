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



df=pd.read_csv('/home/kostis/Desktop/MultimodalAnalysis1/train.csv')


for i in range(len(df)):
	if df['Label'][i]=='positive':
		song=df['url'][i]
		os.system('youtube-dl --extract-audio --audio-format wav -o "/home/kostis/Desktop/MultimodalAnalysis1/positive/%(id)s.%(ext)s" ' + song)


for i in range(len(df)):
	if df['Label'][i]=='negative':
		song=df['url'][i]
		os.system('youtube-dl --extract-audio --audio-format wav -o "/home/kostis/Desktop/MultimodalAnalysis1/negative/%(id)s.%(ext)s" '+ song)
	
