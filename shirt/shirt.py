import sys
import os
from PIL import Image

def main():
    before_filename, after_filename = get_shirt_filenames()
    try:
        filename = "shirt.png"
        shirt = Image.open(filename)
        filename = before_filename
        before = Image.open(before_filename)

        print("shirt", shirt.format, shirt.size, shirt.mode)
        print("before", before.format, before.size, before.mode)

        shirt_width, shirt_height = shirt.size
        before_width, before_height = before.size
        scale = before_width / shirt_width
        after_resize = before.resize((shirt_width, int(before_height / scale)))
        after_resize_crop = after_resize.crop((0,100, 600,700)) # Crop Box: Left-Top (0, 100), Right-Bottom (600, 700)
        after_resize_crop.paste(shirt, (0, 0), shirt)
        after_resize_crop.save(after_filename)

        print("after", after.format, after.size, after.mode)
    except FileNotFoundError:
        sys.exit("Could not open " + filename)

def get_shirt_filenames():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    f1 = os.path.splitext(sys.argv[1])[1].lower()
    f2 = os.path.splitext(sys.argv[2])[1].lower()
    if f1 != ".jpg" and f1 != ".jpeg" and f1 == ".png":
        sys.exit("Files must be of type JPEG or PNG")
    if f1 != f2:
        sys.exti("Files must be of the same type")

    return sys.argv[1], sys.argv[2]

if __name__ == "__main__":
    main()