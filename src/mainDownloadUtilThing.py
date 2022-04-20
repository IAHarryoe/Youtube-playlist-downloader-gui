from __future__ import unicode_literals
import youtube_dl
import json
import os


#set the active directory to the parent directory of the script
os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir("..\\Output")
print(os.getcwd())




ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

ydl = youtube_dl.YoutubeDL({'dump_single_json': False, 'extract_flat' : True})

result = ydl.extract_info('https://youtube.com/playlist?list=PLChTzrq52zsEHdLgeTJ789ugQbevKrlNy', False)

ydl2 = youtube_dl.YoutubeDL(ydl_opts)



for video in result['entries']:
    url = video['url']
    ydl2.download([url])



# print(result)
