import argparse
import os
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_original', help='The path to original image')
    parser.add_argument(
        '-R', '--path_to_result', help='The path to result image'
    )
    parser.add_argument(
        '-H', '--result_height', type=int, help='Result image height'
    )
    parser.add_argument(
        '-W', '--result_width', type=int, help='Result image width'
    )
    parser.add_argument('-S', '--scale', type=float, help='Result image scale')
    args = parser.parse_args()
    if args.scale and (args.result_height or args.result_width):
        raise parser.error('Enter only scala or size')
    return args


def open_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except IsADirectoryError:
        return None
    except FileNotFoundError:
        return None


def get_path_to_result(args, size):
    original_path = args.path_to_original
    result_path = args.path_to_result
    file_path, file_name = os.path.split(original_path)
    if result_path:
        result_path = os.path.join(result_path, file_name)
    else:
        new_file_name = '{}*{} {}'.format(
            size['result_height'], size['result_width'], file_name
        )
        result_path = os.path.join(file_path, new_file_name)
    return result_path


def get_resized_image(image, size):
    resized_image = image.resize(
        (size['result_width'], size['result_height']),
        Image.ANTIALIAS
    )
    return resized_image


def get_new_size(size):
    if size['result_height'] and not size['result_width']:
        size['result_width'] = int(
            size['result_height'] * size['original_width'] /
            size['original_height']
        )
    if size['result_width'] and not size['result_height']:
        size['result_height'] = int(
            size['result_width'] * size['original_height'] /
            size['original_width']
        )
    if size['scale']:
        size['result_width'] = int(size['original_width'] * size['scale'])
        size['result_height'] = int(size['original_height'] * size['scale'])
    return size


def main():
    args = get_args()
    image = open_image(args.path_to_original)
    if not image:
        print('Bad path or image name, please check path original image')
        exit()
    original_width, original_height = image.size
    size = {
        'original_height': original_height,
        'original_width': original_width,
        'result_height': args.result_height,
        'result_width': args.result_width,
        'scale': args.scale,
    }
    size.update(get_new_size(size))
    args.path_to_result = get_path_to_result(args, size)
    resized_image = get_resized_image(image, size)
    resized_image.save(args.path_to_result)


if __name__ == '__main__':
    main()
