import argparse
import os
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_original', help='The path to original image')
    parser.add_argument(
        '-R', '--path_to_result', help='The path to result image',
    )
    parser.add_argument(
        '-H', '--result_height', type=int, help='Result image height',
    )
    parser.add_argument(
        '-W', '--result_width', type=int, help='Result image width',
    )
    parser.add_argument('-S', '--scale', type=float, help='Result image scale')
    args = parser.parse_args()
    if args.scale and (args.result_height or args.result_width):
        raise parser.error('Enter only scala or size')
    if args.scale is None and args.result_height is None \
            and args.result_width is None:
        raise parser.error('You have not entered the size or scale')
    return args


def open_image(image_path):
    try:
        image = Image.open(image_path)
        return image
    except (IsADirectoryError, FileNotFoundError):
        return None


def get_path_to_result(path_to_original,
                       path_to_result,
                       result_height,
                       result_width):
    file_path, full_file_name = os.path.split(path_to_original)
    file_name = full_file_name[:full_file_name.rindex('.')]
    file_format = full_file_name[full_file_name.rindex('.'):]
    if path_to_result:
        result_path = os.path.join(path_to_result, full_file_name)
    else:
        new_file_name = '{}__{}x{}{}'.format(
            file_name, result_height, result_width, file_format,
        )
        result_path = os.path.join(file_path, new_file_name)
    return result_path


def get_resized_image(image, result_width, result_height):
    resized_image = image.resize((result_width, result_height),
                                 Image.ANTIALIAS)
    return resized_image


def get_new_size(original_height, original_width, result_height, result_width,
                 scale):
    if result_height and not result_width:
        result_width = int(result_height * original_width / original_height)
    if result_width and not result_height:
        result_height = int(result_width * original_height / original_width)
    if scale:
        result_width = int(original_width * scale)
        result_height = int(original_height * scale)
    return {'result_width': result_width, 'result_height': result_height}


def main():
    args = get_args()
    image = open_image(args.path_to_original)
    if not image:
        exit('Bad path or image name, please check path original image')
    original_width, original_height = image.size
    size = get_new_size(
        original_height=original_height,
        original_width=original_width,
        result_height=args.result_height,
        result_width=args.result_width,
        scale=args.scale,
    )
    path_to_result = get_path_to_result(
        path_to_original=args.path_to_original,
        path_to_result=args.path_to_result,
        result_height=size['result_height'],
        result_width=size['result_width'],
    )
    resized_image = get_resized_image(
        image,
        result_width=size['result_width'],
        result_height=size['result_height'],
    )
    resized_image.save(path_to_result)


if __name__ == '__main__':
    main()
