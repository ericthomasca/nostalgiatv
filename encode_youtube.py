import os
import yt_dlp
import ffmpeg


def main():
    # Get Videos
    yt_opts = {
        'format': 'best',
        'outtmpl': 'videos/original/%(title)s.%(ext)s',
        'restrictfilenames': True
    }

    ytdl = yt_dlp.YoutubeDL(yt_opts)

    video_link = ['https://www.youtube.com/watch?v=-qQ_HGJqaHQ']

    ytdl.download(video_link)

    # Convert Video
    original_dir = 'videos/original'
    encoded_dir = 'videos/encoded'

    for filename in os.listdir(original_dir):
        input_video = os.path.join(original_dir, filename).replace('\\', '/')
        output_video = os.path.join(encoded_dir, filename).replace('\\', '/')
        print(input_video)
        # output_video = os.path.join(encoded_dir, filename)

        (
            ffmpeg
            .input(input_video)
            .filter('scale', 480, -1)
            .crop(107, 480, 640, 480)
            .output(output_video)
            .run()
        )

    # Delete Originals


if __name__ == '__main__':
    main()
