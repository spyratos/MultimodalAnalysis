# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:57:19 2018

@author: kostis
"""

import youtube_dl
import pandas as pd
import shutil
import os
import os.path
from pathlib import Path, PureWindowsPath
import sys
from sklearn.metrics import accuracy_score
from pyAudioAnalysis import audioAnalysis as aA
df=pd.read_csv('/home/kostis/Desktop/MultimodalAnalysis1/train.csv')
song=df['url'][1]
os.system('youtube-dl --extract-audio --audio-format wav -o "/home/kostis/Desktop/MultimodalAnalysis1/toclassify/%(id)s.%(ext)s" ' + song)

