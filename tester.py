
import os
import yt_dlp
import time

print("\n\n")

# >>> Startup Text:
print(">>> Please ensure that all YouTube videos in the playlist are uploaded after 2011 <<<\n\n>>> Videos that cannot be processed will be removed after the download is complete <<<\n\n")
time.sleep(2)
print(">>> If using these files in additional audio software, please install FFmpeg to avoid errors at:\nhttps://lame.buanzo.org/ffmpeg64audacity.php \n\n")
time.sleep(2)

# >>> URL input:
def new_func():
    url = (input("Enter the URL of the playlist you want to download: \n>>> "))
    return url

url = new_func()

# >>> Filetype Input:
while True:
    filetype = input("\nEnter the filetype: [mp3 / wav] \n>>> ")
    if filetype == "wav" or filetype == "mp3":
        print("\nValid")
        break
    else:
        print("\nInvalid, please try again. [mp3 / wav]\n") 

# >>> Destination Input:
print("\nEnter the destination (leave blank for current directory)")
destination_path = str(input(">>> "))

print("\n\n")

# >>> Download the files:
print(f'\nDownloading...')


ydl_opts = {
        'ignoreerrors': True,
        'WriteThumbnail': True,
        'download_archive': destination_path + '\\already_downloaded_tracks.txt',
        'format': 'bestaudio',
        'outtmpl': destination_path + '/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': filetype,
            'preferredquality': '192',
        },
            {'key': 'FFmpegMetadata'},
        ],
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)

# >>> Result of success:
print("\nPlaylist has been successfully downloaded.")

time.sleep(1)




