# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:18:43 2018

@author: kostis
"""


def main():
    
    
    
    user_input = input("Enter name of file: ")
    df=pd.read_csv(user_input)
    
    
    ##download only audio
    options = {
        'format':'bestaudio/best',
        'extractaudio':True,
        'audioformat':'mp3',
        'outtmpl': r'''C:\Users\kostis\downloads_dl\positive\%(title)s-%(id)s.%(ext)s''',     #name the file the ID of the video
        'noplaylist':True,
        'nocheckcertificate':True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        for i in range(len(df)):
            if df['Label'][i]=='positive':
                ydl.download([str(df['url'][i])])
                
                
        options = {
        'format':'bestaudio/best',
        'extractaudio':True,
        'audioformat':'mp3',
        'outtmpl': r'''C:\Users\kostis\downloads_dl\negative\%(title)s-%(id)s.%(ext)s''',     #name the file the ID of the video
        'noplaylist':True,
        'nocheckcertificate':True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        for i in range(len(df)):
            if df['Label'][i]=='negative':
                ydl.download([str(df['url'][i])])
            
         
              
   
if __name__ == "__main__":
    import youtube_dl
    import pandas as pd
    import youtube_dl
    import shutil
    import os
    import sys
    main()
    
 