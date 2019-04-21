from pathlib import Path

import pytest
from PIL import Image
import numpy as np

from segmental_app import app


TEST_IMAGE_FOLDER = Path(__file__).parent.joinpath('test_images').resolve()
DUMMY_FILE_FOLDER = Path(__file__).parent.joinpath('test_dummy_files').resolve()

TEST_IMAGE_NAME = "10x10.jpg"
TEST_IMAGE = f"{TEST_IMAGE_FOLDER}/{TEST_IMAGE_NAME}"


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client


def test_post_invalid_request_no_image_returns_400(client):
    response = client.post('/generate_labels')

    assert response.status_code == 400
    assert 'An image file is required' in str(response.data)


def test_post_invalid_request_text_image_returns_400(client):
    data = {'image': open(f'{DUMMY_FILE_FOLDER}/test_file.txt', 'rb')}
    response = client.post('/generate_labels', data=data)

    assert response.status_code == 400
    assert 'Invalid file extension' in str(response.data)


def test_post_valid_request_returns_200_with_json_response(client):
    data = {'image': open(TEST_IMAGE, 'rb')}
    response = client.post('/generate_labels', data=data)

    assert response.status_code == 200
    assert response.content_type == 'application/json'


def test_post_valid_request_returns_json_response_with_array_result_as_list(client):
    data = {'image': open(TEST_IMAGE, 'rb')}
    response = client.post('/generate_labels', data=data)

    assert type(response.json['labels_array']) == list


def test_post_valid_request_returns_same_dimensions_array_as_original_image(client):
    in_size = Image.open(TEST_IMAGE).size
    data = {'image': open(TEST_IMAGE, 'rb')}
    response = client.post('/generate_labels', data=data)

    result_array = np.array(response.json['labels_array'])

    assert result_array.shape == tuple(reversed(in_size))
