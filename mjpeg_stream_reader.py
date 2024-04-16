#!/usr/bin/env python3

import io
import os
from urllib.request import urlopen
from PIL import Image
import argparse

parser = argparse.ArgumentParser(
    prog='MJPEGStreamReader',
    description='Read MJPEG stream and save as image files'
)

default_stream = "http://185.49.169.66:1024/cgi-bin/faststream.jpg?stream=half&fps=15&rand=COUNTER"
parser.add_argument('-s', '--stream', help='URL of the MJPEG stream', default=default_stream)
default_out_dir = "/tmp/"
parser.add_argument('-t', '--target', help='Path of the target dir, dir needs to exist', default=default_out_dir)
default_buffer = 1024
parser.add_argument('-b', '--buffer', help='Read buffer size', default=default_buffer)

args = parser.parse_args()

stream_url = args.stream
stream = urlopen(stream_url)

SOI_MARKER = b'\xff\xd8'
EOF_MARKER = b'\xff\xd9'
READ_BUFFER_SIZE = int(args.buffer)

out_dir = args.target

print("----")
print("Reading stream from: " + stream_url)
print("Writing images to: " + out_dir)
print("----")


def save_image(jpg_bytes, image_index):
    image = Image.open(io.BytesIO(jpg_bytes))
    # image.show()
    filename = f"stream_{image_index}.jpg"
    path = os.path.join(out_dir, filename)
    image.save(path)

input_bytes = bytes()
img_index = 0
while True:
    input_bytes += stream.read(READ_BUFFER_SIZE)
    print("Read " + str(len(input_bytes)) + " bytes")
    a = input_bytes.find(SOI_MARKER)
    b = input_bytes.find(EOF_MARKER)
    print("Found SOI at: " + str(a))
    print("Found EOF at: " + str(b))

    if a != -1 and b != -1:
        jpg_bytes = input_bytes[a:b + 2] # b+2 so that EOF_MARKER is included
        input_bytes = input_bytes[b + 2:]
        print("Remaining bytes " + str(len(input_bytes)))
        save_image(jpg_bytes, img_index)
        img_index += 1
