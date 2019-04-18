from PIL import Image
from matplotlib import pyplot as plt
import cv2
import numpy as np
from numpy import ndarray

from model import Deeplabv3


def generate_image_labels(image: ndarray, trained_width=512, mean_subtraction_value=127.5):
    # resize to max dimension of images from training dataset
    w, h, _ = image.shape
    ratio = float(trained_width) / np.max([w, h])
    resized_image = cv2.resize(image, (int(ratio * h), int(ratio * w)))

    # apply normalization for trained dataset images
    resized_image = (resized_image / mean_subtraction_value) - 1.

    # pad to square image to match training images
    pad_x = int(trained_width - resized_image.shape[0])
    pad_y = int(trained_width - resized_image.shape[1])
    resized_image = np.pad(resized_image, ((0, pad_x), (0, pad_y), (0, 0)), mode='constant')

    # make prediction
    deeplab_model = Deeplabv3()
    res = deeplab_model.predict(np.expand_dims(resized_image, 0))
    labels = np.argmax(res.squeeze(), -1)

    # resize back to original
    labels = np.resize(labels, (trained_width - pad_x, trained_width - pad_y))

    return labels


input_image = '/Users/Ben/PycharmProjects/segmental/test/test_images/cat_dog.jpg'

img_array = np.array(Image.open(input_image))

result = generate_image_labels(img_array)

plt.imshow(result)
plt.waitforbuttonpress()