from __future__ import unicode_literals
import youtube_dl
import os
import time
import tkinter as tk
import threading

#top level window
frame = tk.Tk("Downloader")
frame.title = "Downloader"
frame.geometry("400x100")




def downloadAudioFromPlaylist(playlist:str):
    #set the active directory to the parent directory of the script
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.chdir("..\\Output")
    print(os.getcwd())
    #creates a new folder for the output named after the current time
    currenttime = time.strftime("%Y-%m-%d_%H-%M-%S")
    os.mkdir(currenttime)
    os.chdir(currenttime)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    ydl = youtube_dl.YoutubeDL({'dump_single_json': False, 'extract_flat' : True})

    result = ydl.extract_info(playlist, False)

    ydl2 = youtube_dl.YoutubeDL(ydl_opts)

    for video in result['entries']:
        url = video['url']
        ydl2.download([url])

def downloadAudioStartThread(url):
    thread = threading.Thread(target=downloadAudioFromPlaylist, args=(url,))
    thread.start()

def downloadAudioGUI():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text="Downloading...")
    downloadAudioStartThread(inp)
    lbl.config(text="Thread started")


inputtxt = tk.Text(frame, height=1, width=80)

inputtxt.pack()

start_download = tk.Button(frame, text="Download", command=downloadAudioGUI)
start_download.pack()

#label creation
lbl = tk.Label(frame, text="")
lbl.pack()
frame.mainloop()