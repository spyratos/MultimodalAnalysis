# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:40:10 2018

@author: kostis
"""

def main():
	mtwin=float(raw_input('Enter mid term window:'))
	mtmove=float(raw_input('Enter mid term step:'))
	stwin=float(raw_input('Enter short term window:'))
	stmove=float(raw_input('Enter short term step:'))
	aT.featureAndTrain(['/home/kostis/Desktop/MultimodalAnalysis/negative','/home/kostis/Desktop/MultimodalAnalysis/positive'], mtwin, mtmove, stwin, stmove, "svm", "svm_inter")

if __name__ == "__main__":
    import youtube_dl
    import pandas as pd
    import youtube_dl
    import shutil
    import os
    import sys
    from pyAudioAnalysis import audioTrainTest as aT
    main()
