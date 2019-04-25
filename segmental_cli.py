from segmentation.segmentation_utils import generate_image_labels

from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import click


@click.command()
@click.option('--input_img', '-i', help='Input image file.  JPEG and PNG are supported.', type=click.Path(),
              required=True)
def segmental_cli(input_img):
    img_array = np.array(Image.open(input_img))

    result = generate_image_labels(img_array)

    plt.imshow(result)
    plt.waitforbuttonpress()


if __name__ == "__main__":
    segmental_cli()

