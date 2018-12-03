# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:57:19 2018

@author: kostis
"""
def main():
    user_input = input("Enter ID of youtube video: ")
    url='https://www.youtube.com/watch?v='+user_input
    
    options = {
        'format':'bestaudio/best',
        'extractaudio':True,
        'audioformat':'mp3',
        'outtmpl': r'''C:\Users\kostis\downloads_dl\toclassify\%(id)s.%(ext)s''',     #name the file the ID of the video
        'noplaylist':True,
        'nocheckcertificate':True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([str(user_input)])
     
   
    
    data_folder = PureWindowsPath('downloads_dl/toclassify/')
    filename= user_input + str('.wav')
    file_to_open = data_folder / filename
    print(aT.fileClassification(file_to_open, "svm_interviews","svm"))
    
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
    
    
