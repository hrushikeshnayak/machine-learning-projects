# Image Colorization using Deep Learning

This Python script demonstrates the process of colorizing black and white images using deep learning techniques. It utilizes a pre-trained convolutional neural network (CNN) model to automatically colorize grayscale images.

## Installation

1. Download the pre-trained model file [colorization_release_v2.caffemodel](https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1) and place it in the `model` directory.

2. Install the required dependencies:

    ```bash
    pip install numpy opencv-python matplotlib
    ```

## Usage

1. Make sure you have grayscale images that you want to colorize. Place them in the `images` directory or specify their paths in the script.


2. The script will load the pre-trained model, colorize the specified black and white images, and display the results.

## Details

- The script uses OpenCV to load and process images.
- It utilizes a pre-trained Caffe model for image colorization. The model file (`colorization_release_v2.caffemodel`) should be downloaded separately.
- Grayscale images are converted to LAB color space before being fed into the colorization model. After colorization, the LAB image is converted back to RGB.
- The colorized images are displayed using Matplotlib.
<img width="930" alt="image" src="https://github.com/hrushikeshnayak/machine-learning-projects/assets/96150298/f23ad5fc-e89b-4560-beb0-ac154e100ef4">

## Acknowledgments

- The colorization model used in this project is based on the work by Zhang et al. (2016). For more details, refer to their paper: [Colorful Image Colorization](https://arxiv.org/abs/1603.08511).
- This project was inspired by the [colorization.py](https://github.com/opencv/opencv/blob/master/samples/dnn/colorization.py) script from the OpenCV repository.
