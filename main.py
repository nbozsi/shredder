import click
from image_shredder import shredder
from PIL import Image
import os


def potential_filenames(filename):
    extensions = {"jpg", "png", "jfif"}

    for ext in extensions:
        yield f"{filename}.{ext}"


def try_options(image_filename):
    # maybe only the fileformat is wrong, so try out some others
    image_name = image_filename.split(".")[0]  # cuts down the file extension
    for image_filename in potential_filenames(image_name):
        if os.path.exists(image_filename):
            ok = input(f"Did u mean {image_filename}? (Y/n) ").lower()
            if ok == "" or ok == "y":
                return Image.open(image_filename), image_filename
    print("Nope")


@click.command()
@click.argument("filename")
@click.option('-c', "--count", default=2, help="Number of reshreds", show_default=True)
@click.option('-s', "--stripes", default=200, help="Number of the stripes", show_default=True)
@click.option('-o', "--output", default=None, help="Name of the output file")
@click.option('-f', "--force", is_flag=True, default=False, help="Forces your args, no help finding files/rounding count etc..")
def hello(filename, count, stripes, output, force):

    if os.path.exists(filename) or force:
        input_image = Image.open(filename)
    else:
        print("This file does not exists.")
        input_image, filename = try_options(filename)

    if count % 2 != 0 and not force:
        print("Count is odd, so the output image will be stretched.")
        ok = input(f"Round it to {count+1}? (Y/n) ").lower()
        if ok == "" or ok == "y":
            count += 1

    if stripes % count != 0 and not force:
        print("Number of stripes is not divisibel by count, so the result images will slightly differ in width.")
    output_image = shredder(input_image, count, stripes)
    if output:
        output_image.save(output)
    else:
        name, extension = filename.split(".")
        output_image.save(f"{name}_shredded_{count}-{stripes}.{extension}")


if __name__ == "__main__":
    hello()
