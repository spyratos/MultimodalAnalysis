# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:57:19 2018

@author: kostis
"""

#python audioAnalysis.py segmentClassifyFile -i /home/kostis/Desktop/MultimodalAnalysis1/toclassify1/HUjn6XR8lBI.wav --model svm --modelName /home/kostis/Desktop/MultimodalAnalysis1/svm_inter 

from pyAudioAnalysis import audioSegmentation as aS
import numpy

mt_step=0.2
cls=aS.speakerDiarization("/home/kostis/Desktop/MultimodalAnalysis1/toclassify1/HUjn6XR8lBI.wav", n_speakers=0, mt_size=2.0, mt_step=0.2, st_win=0.05, lda_dim=35, plot_res=False)
print(numpy.array(range(len(cls)))*mt_step+mt_step/2.0)
print("len array:",len(numpy.array(range(len(cls)))*mt_step+mt_step/2.0))
print(cls)
print("len cls:",len(cls))

temp=(numpy.array(range(len(cls)))*mt_step+mt_step/2.0)
print(temp)

file_object  = open("test.segments", "w")
for i in range(len(temp)):
    if(i+1==len(temp)):
        break;
    file_object.write(str(float(temp[i]))+","+str(float(temp[i+1]))+","+str(cls[i])+"\n") 

file_object.close() 
