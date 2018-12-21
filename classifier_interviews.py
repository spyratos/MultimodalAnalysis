# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:40:10 2018

@author: kostis
"""

def main():
    aT.featureAndTrain([r'''C:\Users\kostis\downloads_dl\negative''',r'''C:\Users\kostis\downloads_dl\positive'''], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svm_inter")

if __name__ == "__main__":
    import youtube_dl
    import pandas as pd
    import youtube_dl
    import shutil
    import os
    import sys
    from pyAudioAnalysis import audioTrainTest as aT
    main()
