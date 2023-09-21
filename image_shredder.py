from PIL import Image
import os


def make_strips(im, n_strings):
    """Splits the image into strips and make two images from them like 'one here, one there'"""
    WIDTH, HEIGHT = im.size
    if HEIGHT % 2 == 1:
        im = im.crop((0, 0, WIDTH, HEIGHT - 1))
        HEIGHT -= 1
    print(im.format, im.size, im.mode)
    new_image = Image.new("RGB", (WIDTH * 2, HEIGHT // 2))

    for i in range(0, n_strings):

        a = int((HEIGHT/2)*i//n_strings*2)
        c = int((HEIGHT/2)*(i+1)//n_strings*2)
        b = int((c+a)//2)

        region1 = im.crop((0, a, WIDTH, b))
        region2 = im.crop((0, b, WIDTH, c))

        new_image.paste(region1, (0, a//2, WIDTH, b - a//2))
        new_image.paste(region2, (WIDTH, a//2, WIDTH*2, b - a//2))

    return new_image


def shredder(image, count, strips):
    for i in range(count):
        image = make_strips(image, strips)
        if i % 2 == 0:
            image = image.transpose(Image.Transpose.ROTATE_90)
        else:
            image = image.transpose(Image.Transpose.ROTATE_270)
    return image


if __name__ == "__main__":
    name = input()
    im = Image.open(name)
    ujra = int(input("Times I reshred the image: "))
    p = int(input("Number of strips in one shred: "))
    p = p // 2 * 2
    folder = name.split(".")[0]
    os.mkdir(f"{folder}_{p}")
    output = f"{folder}_{p}/{folder}.png"
    shredder(im, ujra, p).save(output)
