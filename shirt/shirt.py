import sys
import os
from PIL import Image

def main():
    before_filename, after_filename = get_shirt_filenames()
    try:
        filename = "shirt.png"
        cs50 = Image.open(filename)
        filename = before_filename
        before = Image.open(before_filename)

        print("cs50", cs50.format, cs50.size, cs50.mode)
        print("before", before.format, before.size, before.mode)

        cs50_width, cs50_height = cs50.size
        before_width, before_height = before.size

        width_ratio = before_width / cs50_width

        after = before.resize((cs50_width, int(before_height / width_ratio)))
        after_crop = after
#        after_crop = after.crop((0,200, 800, 800))

 #       after_crop.paste(cs50, (0, 0), cs50)

        after_crop.save(after_filename)

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