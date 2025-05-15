# Any2Any Image Converter

A fast, local, and user-friendly tool to convert images between popular formats with optional professional lossless mode. No cloud upload—your images stay on your machine!

## Features
- **Convert between popular image formats:** JPEG, PNG, BMP, GIF, TIFF, WebP, and more
- **Professional lossless mode:** For high-res photography and maximum quality
- **Interactive mode:** Guided prompts for easy use
- **Batch conversion:** Convert multiple images at once
- **Progress bar and fun messages**
- **100% local processing**

## Requirements
- Python 3.7+
- [Pillow](https://python-pillow.org/) (for image processing)
- [tqdm](https://tqdm.github.io/) (for progress bars)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage

### Command-Line Mode
Convert images directly from the command line:
```bash
python any2any_converter.py input1.jpg input2.png -f png -o output_dir
```

**Options:**
- `-f`, `--format`      Output image format (jpeg, jpg, png, bmp, gif, tiff, webp)
- `-o`, `--output-dir`  Output directory (default: `converted`)
- `--lossless`          Enable professional lossless mode (recommended for high-res photography)

### Interactive Mode
If you omit required arguments or use `--interactive`, you'll be guided through the process:
```bash
python any2any_converter.py --interactive
```

## Example
Convert all JPEGs in a folder to PNG with lossless mode:
```bash
python any2any_converter.py *.jpg -f png --lossless
```

## Output
Converted images are saved in the specified output directory (default: `converted`).

## Supported Formats
- Input: Any format supported by Pillow (JPEG, PNG, BMP, GIF, TIFF, WebP, etc.)
- Output: jpeg, jpg, png, bmp, gif, tiff, webp

## License
Apache 2.0

## Author
- Alexander Scott for the BrowserVM Project

---
*Reticulating splines...*
