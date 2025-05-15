.t# Any2Any Image Converter

A fast, local, and user-friendly tool to convert images between popular formats with optional professional lossless mode. No cloud upload—your images stay on your machine!

## Features
- **Convert between popular image formats:** JPEG, PNG, BMP, GIF, TIFF, WebP, and more
- **Professional lossless mode:** For high-res photography and maximum quality
- **Interactive mode:** Guided prompts for easy use
- **Batch conversion:** Convert multiple images at once
- **Progress bar and fun messages**
- **100% local processing**

## Video Conversion
- **Convert between popular video formats:** MP4, AVI, MOV, MKV, WebM
- **Batch video conversion:** Convert multiple videos at once

## Requirements
- Python 3.7+
- [Pillow](https://python-pillow.org/) (for image processing)
- [tqdm](https://tqdm.github.io/) (for progress bars)
- [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) (for video conversion)
- [FFmpeg](https://ffmpeg.org/) (must be installed on your system)

Install dependencies with:
```bash
pip install -r requirements.txt
```

Make sure FFmpeg is installed and available in your PATH. On Ubuntu/Debian:
```bash
sudo apt update
sudo apt-get install ffmpeg
```

## Usage

### Command-Line Mode
Convert images or videos directly from the command line:
```bash
# Image conversion
python any2any_converter.py input1.jpg input2.png -f png -o output_dir

# Video conversion
python any2any_converter.py input1.mp4 input2.avi --video --video-format mkv -o output_dir
```

**Options:**
- `-f`, `--format`         Output image format (jpeg, jpg, png, bmp, gif, tiff, webp)
- `--video`                Convert video files instead of images
- `--video-format`         Output video format (mp4, avi, mov, mkv, webm)
- `-o`, `--output-dir`     Output directory (default: `converted`)
- `--lossless`             Enable professional lossless mode (images only)

### Interactive Mode
If you omit required arguments or use `--interactive`, you'll be guided through the process:
```bash
python any2any_converter.py --interactive
```

## Example
Convert all MP4s in a folder to MKV:
```bash
python any2any_converter.py *.mp4 --video --video-format mkv
```

## Output
Converted files are saved in the specified output directory (default: `converted`).

## Supported Formats
- **Image Input:** Any format supported by Pillow (JPEG, PNG, BMP, GIF, TIFF, WebP, etc.)
- **Image Output:** jpeg, jpg, png, bmp, gif, tiff, webp
- **Video Input/Output:** mp4, avi, mov, mkv, webm

## License
Apache 2.0

## Author
- Alexander Scott for the BrowserVM Project

---
*Reticulating splines...*
