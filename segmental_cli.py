from segmentation.segmentation_utils import generate_image_labels

from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import click


@click.command()
@click.argument('image_path')
def segmental_cli(image_path):
    img_array = np.array(Image.open(image_path))

    result = generate_image_labels(img_array)

    plt.imshow(result)
    plt.waitforbuttonpress()


if __name__ == "__main__":
    segmental_cli()

