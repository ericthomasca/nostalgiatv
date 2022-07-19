from __future__ import unicode_literals
import sys
import youtube_dl
import ffmpeg


def main():
    yt_opts = {
        'format': 'best',
        'outtmpl': 'videos/unprocessed/%(title)s.%(ext)s',
        'restrictfilenames': True,
    }

    ytdl = youtube_dl.YoutubeDL(yt_opts)

    video_link = ['https://www.youtube.com/watch?v=TIfAkOBMf5A']

    ytdl.download(video_link)


if __name__ == '__main__':
    main()
