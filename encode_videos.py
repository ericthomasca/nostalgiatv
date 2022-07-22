import os
import yt_dlp
import ffmpeg
import sys


def main():
    # Get Videos
    yt_opts = {
        'format': 'best',  # 720p
        'outtmpl': 'videos/original/%(title)s.%(ext)s',
        'restrictfilenames': True
    }

    ytdl = yt_dlp.YoutubeDL(yt_opts)
    video_link = [sys.argv[1]]
    ytdl.download(video_link)

    # Convert Video
    original_dir = 'videos/original'
    encoded_dir = 'videos/encoded'

    for filename in os.listdir(original_dir):
        input_video = os.path.join(original_dir, filename)
        output_video = os.path.join(encoded_dir, filename)

        input_video_probe = ffmpeg.probe(input_video)['streams'][0]
        print(input_video_probe)
        aspect_ratio = input_video_probe['display_aspect_ratio']
        input_width = input_video_probe['width']
        input_height = input_video_probe['height']
        output_width = input_height * 4 / 3
        output_height = input_height
        black_bar_width = (input_width - output_width) / 2

        if aspect_ratio == '16:9':
            (
                ffmpeg
                .input(input_video)
                .crop(black_bar_width, 0, output_width, output_height)  # Remove black bars
                .filter('scale', 640, -1)  # Resize to 640x480
                .output(output_video)
                .run(overwrite_output=True)
            )
        elif aspect_ratio == '4:3':
            (
                ffmpeg
                .input(input_video)
                .filter('scale', 640, -1)  # Resize to 640x480
                .output(output_video)
                .run(overwrite_output=True)
            )
        else:
            print('Can\'t process video. Aspect ratio needs to be 16:9 or 4:3')

        os.remove(input_video)


if __name__ == '__main__':
    main()
