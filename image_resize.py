import argparse
import os
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_original', type=str, help='The path to original image')
    parser.add_argument('-R', '--path_to_result', type=str, help='The path to result image')
    parser.add_argument('-H', '--result_height', type=int, help='Result image height')
    parser.add_argument('-W', '--result_width', type=int, help='Result image width')
    parser.add_argument('-S', '--scale', type=float, help='Result image scale')
    args = parser.parse_args()
    args_dict = {
        'path_to_original': args.path_to_original,
        'result_height': args.result_height,
        'result_width': args.result_width,
        'scale': args.scale,
        'path_to_result': args.path_to_result,
    }
    return args_dict


def open_image(image_path):
    if os.path.exists(image_path):
        image = Image.open(image_path)
        return image


def get_path_ro_result(args):
    original_path = args['path_to_original']
    result_path = args['path_to_result']
    file_path, file_format = os.path.splitext(original_path)
    file_name = os.path.basename(original_path)
    if result_path:
        result_path = '{}{}'.format(result_path, file_name)
    else:
        result_path = ('{} {}*{}{}'.format(file_path, args['new_width'], args['new_height'], file_format))
    return result_path


def get_resized_image(image, args):
    new_width = args['new_width']
    new_height = args['new_height']
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_image


def get_new_size(args):
    new_width = args['result_width']
    new_height = args['result_height']
    scale = args['scale']
    original_width = args['original_width']
    original_height = args['original_height']
    if new_height and not new_width:
        new_width = int(new_height * original_width / original_height)
    if new_width and not new_height:
        new_height = int(new_width * original_height / original_width)
    if scale:
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
    new_size = {'new_width': new_width, 'new_height': new_height}
    return new_size


def main():
    args = get_args()
    image = open_image(args['path_to_original'])
    if not image:
        print('Bad path or image name, please check path original image')
    else:
        if args['scale'] and args['']:
            print('You enter scale, the height and width will be ignored')
        original_width, original_height = image.size
        args.update({'original_width': original_width, 'original_height': original_height})
        new_size = get_new_size(args)
        for key, value in new_size.items():
            args[key] = value
        args['path_to_result'] = get_path_ro_result(args)
        resized_image = get_resized_image(image, args)
        resized_image.save(args['path_to_result'])


if __name__ == '__main__':
    main()
