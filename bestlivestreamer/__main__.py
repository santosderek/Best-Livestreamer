"""
Script by: Derek Santos
Mainly for personal use.

[FFMPEG]
To convert .ts to .mkv use ffmpeg:
ffmpeg -i LiveStream.ts -vcodec copy -qscale 0 -acodec copy -f matroska output.mkv

"""

from argparse import ArgumentParser
from subprocess import run
from os import chdir
import logging

""" State and Examine Given Working Directory """
WORKING_DIR = r'.'

""" Change Working Directory """
chdir(WORKING_DIR)

""" Livestreamer Command """
LIVESTREAMER_COMMAND = 'livestreamer "{url}" best --hls-live-edge 99999 -o {title}.ts'


""" Setting up logging """
logging.basicConfig(level=logging.DEBUG,
                    format="[BestLivestreamer] [%(levelname)s] %(asctime)s: %(message)s",
                    datefmt='%I:%M:%S %p')

LOGGER = logging.getLogger('bestlivestreamer')


def parse_arguments():
    """ Parse Arguments at startup """
    parser = ArgumentParser(description='Feed me stream url.')
    parser.add_argument('url', metavar='url', type=str)
    parser.add_argument('-t',
                        '--title',
                        metavar='title',
                        help='Change File Name',
                        type=str)
    return parser.parse_args()


def download_url(url: str, title: str):
    """ Create subprocess of Youtube-DL command """
    command = LIVESTREAMER_COMMAND.format(url=url, title=title)
    run(command, shell=True)


def main():
    """ Main function """

    try:
        arguments = parse_arguments()

        title = 'LiveStream'

        # If title was not defined, use default title
        if not arguments.title:
            LOGGER.info('No Title Given... ')
            LOGGER.info('Default file title: {}'.format(title))

        else:
            title = arguments.title

        download_url(arguments.url, title)
    except Exception as e:
        pass


if __name__ == "__main__":
    main()
