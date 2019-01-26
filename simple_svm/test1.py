def main():
    user_input = raw_input("Enter ID of youtube video: ")
    url='https://www.youtube.com/watch?v='+user_input
    
    options = {
        'format':'bestaudio/best',
        'extractaudio':True,
        'audioformat':'mp3',
        'outtmpl': '/home/kostis/Desktop/MultimodalAnalysis1/toclassify/%(id)s.%(ext)s',     #name the file the ID of the video
        'noplaylist':True,
        'nocheckcertificate':True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([str(url)])
     
   
    
    
    print(aT.fileClassification("/home/kostis/Desktop/MultimodalAnalysis1/toclassify/"+str(user_input)+".mp3", "svm_inter","svm"))
    
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
    
    