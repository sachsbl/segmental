Segmental
=======

An example application that runs Google's DeepLabv3+ to perform Semantic Image Segmentation.  It is backed by the latest
Tensorflow/Keras distributions.  Segmental can be run as a CLI, but is also Dockerized and can be run as a Flask app in 
a Docker container.  The goal of this project is to provide an example of how to productionize the latest Deep Learning 
tech, and provide a QuickStart example for people interested in this approach.  I do not claim that the segmentation
results are that amazing, but the model can be re-trained to provide better results and the framework provided will 
still work well.  

Network/Model
-----
Segmental uses Google's DeepLabv3+ with pre-trained weights.  It supports MobileNetv2 (and perhaps Xception with some 
mods).  The latest (currently Alpha) release of Tensorflow (2.0 Alpha) is used.  

This work builds on the original models here:
https://github.com/bonlime/keras-deeplab-v3-plus
 

Running the CLI
-----
Download the repo and build an environment using pip.  ONLY Python 3.7+ is supported.  

```pip install -r requirements_cli.txt```

Run "python segmental_cli.py -- help" for the CLI interface.

```
Options:
  -i, --input_img PATH  Input image file.  JPEG and PNG are supported.
                        [required]
  --help                Show this message and exit.

```

Docker
-----
The Dockerfile provided can be used to build a Docker image that runs Segmental as a Flask application.  See the tests
for example usage.  Basically it takes an image file as a parameter and returns the resulting array as a json list. 
Gunicorn is used for a more robust web server.  You can also pull my Docker image:

```
docker pull sachsbl/segmental
docker run -p 80:5000 segmental
``` 


Tests
-----
Automated tests can used to verify functionality.  
These can be run with PyTest, which may need to be installed separately.  

Make sure the project's directory is part of your PYTHONPATH:

``` export PYTHONPATH="${PYTHONPATH}:/path/to/segmental"```

Install PyTest and other dependencies
```
pip install -r requirements_test.txt
```

Run the following from the root directory to run all tests:

```
pytest test
```


Example Result
-----
![Alt text](test/test_images/dog_baxter.jpg?raw=true "Baxter")
![Alt text](examples/baxter_result.jpg?raw=true "Baxter Segmented")

