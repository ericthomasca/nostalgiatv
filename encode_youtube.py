import os
import yt_dlp
import ffmpeg


def main():
    # Get Videos
    yt_opts = {
        'format': '22',  # 720p
        'outtmpl': 'videos/original/%(title)s.%(ext)s',
        'restrictfilenames': True
    }

    ytdl = yt_dlp.YoutubeDL(yt_opts)

    # TODO change to argument
    video_link = ['https://www.youtube.com/watch?v=-qQ_HGJqaHQ']
    ytdl.download(video_link)

    # Convert Video
    original_dir = 'videos/original'
    encoded_dir = 'videos/encoded'

    for filename in os.listdir(original_dir):
        input_video = os.path.join(original_dir, filename)
        # print(ffmpeg.probe(input_video))
        output_video = os.path.join(encoded_dir, filename)
        (
            ffmpeg
            .input(input_video)
            .crop(160, 0, 960, 720)  # Remove black bars
            .filter('scale', 640, -1)  # Add scaling when target resolution is known
            .output(output_video)
            .run(overwrite_output=True)
        )

        del input_video


if __name__ == '__main__':
    main()
