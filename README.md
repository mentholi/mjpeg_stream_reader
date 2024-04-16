# MJPEG Stream reader

Reads MJPEG stream and saves frames as JPG images to target directory.

## Installation and usage

1. Git clone this repo
2. Create virtualenv `mkvirtualenv mjpeg_stream_reader --python=~/.pyenv/versions/3.11/bin/python`
3. Install requirements `pip install -r requirements.txt`

Run the script:

```bash
./mjpeg_stream_reader.py --help
    usage: MJPEGStreamReader [-h] [-s STREAM] [-t TARGET] [-b BUFFER]

    Read MJPEG stream and save as image files

    options:
    -h, --help            show this help message and exit
    -s STREAM, --stream STREAM
                            URL of the MJPEG stream
    -t TARGET, --target TARGET
                            Path of the target dir, dir needs to exist
    -b BUFFER, --buffer BUFFER
                            Read buffer size
```

If you run the script without any arguments, it will use the default target stream and output to `/tmp`.