# Image Resizer

The script accepts an image and places an image with a new size where
the user or next to the source says. It has a mandatory argument -
the **path to the original** picture. And a few optional: **width** - width
of the resulting image, **height** - its height, **scale** - how many times
to increase the image (maybe less than 1), **output** - where to put the
resulting file.

# How to run

Open the terminal, go to the directory where the file is located,
run **"python image_resize.py"**, if python 3 as not default
try **"python3 image_resize.py"** and enter the keys.

#### Command lines keys:

##### Positional arguments:
* **path_to_original** The path to original image
##### Optional values
* **-R, --path_to_result** The path to result image
* **-H, --result_height** Result image height
* **-W, --result_width** Result image width
* **-S, --scale** Result image scale

**_if you enter only width, or only height, other value will calculate
automatically with initial image proportions_**

#### Example to run

```bash
$ python image_resize.py [path to original] -R [path to save resized image] \
-H [int] -W [int] -S [float]

```

# How to Install

Python 3 should be already installed.
Then use **pip** (or **pip3** if there is a conflict with old Python 2 setup)
to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
