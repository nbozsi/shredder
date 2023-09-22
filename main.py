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
@click.option('-s', "--stripes", default=(200, 200), multiple=True, help="Number of the stripes", show_default=True)
@click.option('-o', "--output", default=None, help="Name of the output file")
@click.option("--squared", is_flag=True, default=False, help="Make the small rectangles squares")
@click.option('-w', is_flag=True, default=False, help="No help finding files/rounding count and no warnings etc..")
def hello(filename, count, stripes, output, squared, w):

    # filename
    if os.path.exists(filename) or w:
        input_image = Image.open(filename)
    else:
        print("This file does not exists.")
        input_image, filename = try_options(filename)

    # count
    if count % 2 != 0 and not w:
        print("Count is odd, so the output image will be stretched.")
        ok = input(f"Round it to {count+1}? (Y/n) ").lower()
        if ok == "" or ok == "y":
            count += 1

    # stripes
    if len(stripes) == 1:
        stripes += stripes

    # if stripes % count != 0 and not w:
    #    print("The number of stripes is not divisible by count, so the result images will slightly differ in width.")

    # squared
    if squared:
        print(stripes)
        if len(stripes) > 1:
            print("Can't make it square like this, 2nd stripes arg is ignored")
            stripes = (stripes[0],)
        d = stripes[0]
        WIDTH, HEIGHT = input_image.size
        stripes += ((2 * WIDTH*stripes[0])//HEIGHT,)

    output_image = shredder(input_image, count, *stripes)
    if output:
        output_image.save(output)
    else:
        name, extension = filename.split(".")
        output_image.save(
            "{}_shredded_{}-{}-{}.{}".format(name, count, *stripes, extension))


if __name__ == "__main__":
    hello()
