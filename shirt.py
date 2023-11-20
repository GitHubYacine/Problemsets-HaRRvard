from PIL import Image, ImageOps
import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 3:
    try:
        if sys.argv[1].endswith((".jpg", ".jpeg", ".png")) and sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
            image = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            size = shirt.size
            sized_image = ImageOps.fit(image=image,size=size)
            sized_image.paste(shirt, shirt)
            sized_image.save(sys.argv[2])
        else:
            sys.exit("Invalid input. Make sure Input and Output have same extensions.")
    except FileNotFoundError:
        sys.exit("Could not find said file")
