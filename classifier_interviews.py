# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:40:10 2018

@author: kostis
"""

def main():
    aT.featureAndTrain(['/home/kostis/Desktop/MultimodalAnalysis1/negative','/home/kostis/Desktop/MultimodalAnalysis1/positive'], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svm_inter")

if __name__ == "__main__":
    import youtube_dl
    import pandas as pd
    import youtube_dl
    import shutil
    import os
    import sys
    from pyAudioAnalysis import audioTrainTest as aT
    main()
