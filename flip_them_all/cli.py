"""
Usage:
    flip_them_all [options] <input-directory> <output-directory>

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
    --quality=<n>    Quality 1 highest to 31 lowest [default: 1]
"""
from docopt import docopt
import logging
import sys
import os
import glob
from subprocess import Popen

from flip_them_all.conf import settings

logger = logging.getLogger('cli')


def ensure_directory(d):
    if not os.path.exists(d):
        os.makedirs(d)
    elif not os.path.isdir(d):
        raise Exception("The path {0} is not a directory")


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed_args = docopt(__doc__, args)
    if parsed_args['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    elif parsed_args['--verbose']:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    if settings.ffmpeg is None:
        logger.error("Please install ffmpeg")
        return 1

    input_directory = parsed_args['<input-directory>']
    input_directory = os.path.abspath(os.path.expanduser(input_directory))
    ensure_directory(input_directory)
    output_directory = parsed_args['<output-directory>']
    output_directory = os.path.abspath(os.path.expanduser(output_directory))
    ensure_directory(output_directory)
    quality = parsed_args['--quality']
    for f in glob.glob(os.path.join(input_directory, '*')):
        output_file = os.path.join(output_directory, os.path.basename(f))
        if os.path.exists(output_file):
            continue
        logger.info("Flipping %s", f)
        p = Popen([settings.ffmpeg, "-i", f, "-vf", "hflip,vflip", "-q:v", quality, output_file])
        p.wait()
    return 0
