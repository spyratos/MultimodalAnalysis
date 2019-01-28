# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:57:19 2018

@author: kostis
"""
def main():
    
        
   


    df=pd.read_csv('/home/kostis/Desktop/MultimodalAnalysis1/test.csv')


   # for i in range(len(df)):
    #   song=df['url'][i]
     #  os.system('youtube-dl --extract-audio --audio-format wav -o "/home/kostis/Desktop/MultimodalAnalysis1/toclassify/%(id)s.%(ext)s" ' + song)


	 
    
    predicted=aA.classifyFolderWrapper("/home/kostis/Desktop/MultimodalAnalysis1/toclassify/","svm","/home/kostis/Desktop/MultimodalAnalysis/simple_svm/svm_inter",outputMode=True)
    df['id'] = df['url'].str.extract('v=([^&]*)', expand=True)
    actual=[]
    pred=[]
    print(df.head())
    for i in range(len(df)):
        actual.append(df['Label'][i])
        pred.append(predicted[df['id'][i]])
    print(actual)
    print("\n")
    print(pred)
    print accuracy_score(actual, pred)

if __name__ == "__main__":
    import youtube_dl
    import pandas as pd
    import shutil
    import os
    import os.path
    from pathlib import Path, PureWindowsPath
    import sys
    from sklearn.metrics import accuracy_score
    from pyAudioAnalysis import audioAnalysis as aA
    main()

    
