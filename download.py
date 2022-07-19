from __future__ import unicode_literals
import youtube_dl


def main():
    def dl_video(video_link):
        yt_opts = {
            'format': '397',
            'outtmpl': 'videos/unprocessed/%(title)s.%(ext)s',
            'restrictfilenames': True
        }

        ytdl = youtube_dl.YoutubeDL(yt_opts)
        ytdl.download(video_link)


if __name__ == '__main__':
    main()
