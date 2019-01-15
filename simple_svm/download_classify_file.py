# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:57:19 2018

@author: kostis
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:57:19 2018

@author: kostis
"""
def main():
    user_input = input("Enter ID of youtube video: ")
    url='https://www.youtube.com/watch?v='+user_input
    
   
  
    
    os.system('youtube-dl --extract-audio --audio-format mp3 -o "/home/kostis/Desktop/MultimodalAnalysis/simple_svm/toclassify/%(id)s.%(ext)s" ' + url)
     
    os.system('python audioAnalysis.py classifyFolder -i /home/kostis/Desktop/MultimodalAnalysis/simple_svm/toclassify/ --model svm --classifier /home/kostis/Desktop/MultimodalAnalysis/svm_inter --details')
    

  
if __name__ == "__main__":
    import youtube_dl
    import pandas as pd
    import shutil
    import os
    import os.path
    from pathlib import Path, PureWindowsPath
    import sys
    from pyAudioAnalysis import audioTrainTest as aT
    main()
    
    
