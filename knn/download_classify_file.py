# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:57:19 2018

@author: kostis
"""


import matplotlib.pyplot as plt
import youtube_dl
import pandas as pd
import shutil
import os
import os.path
from pathlib import Path, PureWindowsPath
import sys
from sklearn.metrics import accuracy_score
from pyAudioAnalysis import audioAnalysis as aA
from sklearn.metrics import confusion_matrix
import numpy as np    
import itertools


def plot_confusion_matrix(cm, classes,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    """
    
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
def main():
    

	mtwin=float(raw_input('Enter mid term window:'))
	mtmove=float(raw_input('Enter mid term step:'))
	stwin=float(raw_input('Enter short term window:'))
	stmove=float(raw_input('Enter short term step:'))


	df=pd.read_csv('/home/kostis/Desktop/MultimodalAnalysis/simple_svm/test1.csv')


	# for i in range(len(df)):
	#   song=df['url'][i]
	#   os.system('youtube-dl --extract-audio --audio-format wav -o "/home/kostis/Desktop/MultimodalAnalysis1/toclassify/%(id)s.%(ext)s" ' + song)


	 

	predicted=aA.classifyFolderWrapper("/home/kostis/Desktop/MultimodalAnalysis/toclassify/","knn","/home/kostis/Desktop/MultimodalAnalysis/knn/knn_inter",outputMode=True)
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
	cm = confusion_matrix(actual, pred)
	plt.figure()
	plot_confusion_matrix(cm,['positive','negative'],"KNN \nmid term window: "+str(mtwin)+" mid term step: "+str(mtmove)+" \nshort term window: "+str(stwin)+" short term step "+str(stmove)+"\naccuracy score: %.2f"%float(accuracy_score(actual, pred)))
	plt.show()

if __name__ == "__main__":
	main()

    
