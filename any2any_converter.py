#!/usr/bin/env python3
import os
import sys
import argparse
from PIL import Image
from tqdm import tqdm
import ffmpeg
import secrets

FUNNY_MESSAGES = [
    "Reticulating splines...",
    "Polishing pixels...",
    "Convincing the bits to behave...",
    "Making your images 42% cooler...",
    "Negotiating with color spaces...",
    "Counting all the pixels (just kidding)...",
    "Unleashing the magic smoke...",
    "Telling JPEGs to stop being lossy...",
    "Summoning the lossless gods...",
    "Making your image look professional...",
]

COMMON_FORMATS = ['jpeg', 'jpg', 'png', 'bmp', 'gif', 'tiff', 'webp']
LOSSLESS_FORMATS = ['png', 'tiff', 'webp']
COMMON_VIDEO_FORMATS = ['mp4', 'avi', 'mov', 'mkv', 'webm']


def get_funny_message():
    return secrets.choice(FUNNY_MESSAGES)


def convert_image(input_path, output_path, output_format, lossless=False):
    with Image.open(input_path) as img:
        save_kwargs = {}
        if lossless:
            if output_format == 'webp':
                save_kwargs['lossless'] = True
            if output_format in ['jpeg', 'jpg']:
                save_kwargs['quality'] = 100
                save_kwargs['subsampling'] = 0
        img.save(output_path, format=output_format.upper(), **save_kwargs)


def is_video_file(filename):
    ext = os.path.splitext(filename)[1].lower().lstrip('.')
    return ext in COMMON_VIDEO_FORMATS


def convert_video(input_path, output_path, output_format):
    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path)
            .run(overwrite_output=True, quiet=True)
        )
    except ffmpeg.Error as e:
        raise RuntimeError(f"ffmpeg error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Any-to-any image converter (100% local)")
    parser.add_argument('--interactive', action='store_true', help="Run in interactive mode")
    parser.add_argument('input', nargs='*', help="Input image file(s)")
    parser.add_argument('-o', '--output-dir', default='converted', help="Output directory")
    parser.add_argument('-f', '--format', choices=COMMON_FORMATS, help="Output image format")
    parser.add_argument('--lossless', action='store_true', help="Enable professional lossless mode (recommended for high-res photography)")
    parser.add_argument('--video', action='store_true', help="Convert video files instead of images")
    parser.add_argument('--video-format', choices=COMMON_VIDEO_FORMATS, help="Output video format (mp4, avi, mov, mkv, webm)")
    args = parser.parse_args()

    if args.interactive or not args.input or (not args.format and not args.video_format):
        print("\n--- Any2Any Image/Video Converter (Interactive Mode) ---")
        # Input files
        while True:
            input_files = input("Enter file paths (comma-separated): ").strip()
            if input_files:
                input_list = [f.strip() for f in input_files.split(',') if f.strip()]
                if all(os.path.isfile(f) for f in input_list):
                    break
                else:
                    print("One or more files do not exist. Please try again.")
            else:
                print("Please enter at least one file.")
        args.input = input_list
        # Image or video
        is_video = input("Are these video files? [y/N]: ").strip().lower() == 'y'
        args.video = is_video
        # Output format
        if is_video:
            while True:
                fmt = input(f"Choose output video format {COMMON_VIDEO_FORMATS}: ").strip().lower()
                if fmt in COMMON_VIDEO_FORMATS:
                    args.video_format = fmt
                    break
                else:
                    print("Invalid format. Please try again.")
        else:
            while True:
                fmt = input(f"Choose output image format {COMMON_FORMATS}: ").strip().lower()
                if fmt in COMMON_FORMATS:
                    args.format = fmt
                    break
                else:
                    print("Invalid format. Please try again.")
        # Output directory
        out_dir = input(f"Output directory [{args.output_dir}]: ").strip()
        if out_dir:
            args.output_dir = out_dir
        # Lossless mode (images only)
        if not is_video:
            lossless = input("Enable professional lossless mode? [y/N]: ").strip().lower()
            args.lossless = lossless == 'y'

    os.makedirs(args.output_dir, exist_ok=True)

    if args.video:
        for i, input_path in enumerate(tqdm(args.input, desc="Converting videos", unit="vid")):
            print(get_funny_message())
            base = os.path.splitext(os.path.basename(input_path))[0]
            output_path = os.path.join(args.output_dir, f"{base}.{args.video_format}")
            try:
                convert_video(input_path, output_path, args.video_format)
            except Exception as e:
                print(f"Failed to convert {input_path}: {e}")
        print("\nAll done! Your videos are in:", args.output_dir)
        return

    print("\nProfessional Lossless Mode is {}".format(
        "ENABLED (recommended for high-res photography!)" if args.lossless else "disabled (for smaller files)"
    ))

    for i, input_path in enumerate(tqdm(args.input, desc="Converting images", unit="img")):
        print(get_funny_message())
        base = os.path.splitext(os.path.basename(input_path))[0]
        output_path = os.path.join(args.output_dir, f"{base}.{args.format}")
        try:
            convert_image(input_path, output_path, args.format, lossless=args.lossless)
        except Exception as e:
            print(f"Failed to convert {input_path}: {e}")

    print("\nAll done! Your images are in:", args.output_dir)

if __name__ == "__main__":
    main()
