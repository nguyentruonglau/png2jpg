import argparse
import os
import sys
from tqdm import tqdm
from imutils.paths import list_images
from PIL import Image


def parse_args(args):
    parser = argparse.ArgumentParser("")
    parser.add_argument('--input_dir', type=str, default='./input_data')
    parser.add_argument('--output_dir', type=str, default='./output_data')
    return parser.parse_args(args)


def main(args):
    if not os.path.exists(args.input_dir):
        raise ValueError('[ERROR]: {} not found'.format(args.input_dir))

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    image_paths = list(list_images(args.input_dir))
    if len(image_paths) == 0:
        raise ValueError('[ERROR]: Images in {} not found'.format(args.input_dir))

    print('[INFOR]: Start converting...')

    for i in tqdm(range(len(image_paths))):
        img = Image.open(image_paths[i])
        img.convert('RGB').save(os.path.join(args.output_dir, os.path.basename(image_paths[i]).replace('.png', '.jpg')), 'JPEG')

    print('[INFOR]: Completed converting!')


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])

    print('input_dir=',args.input_dir)
    print('output_dir=',args.output_dir)
   
    main(args)