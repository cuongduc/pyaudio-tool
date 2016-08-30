"""
Download list of audios from Amazon S3
"""
# from utils.s3 import S3
# from utils.data import get_audio_list_from_file
from __future__ import absolute_import

from utils.data import get_audio_list_from_file, get_remote_audio
from utils.urls import get_filename_from_url
#from utils.helpers import var_dump

AUDIO_LIST_INPUT_FILE = 'data/audio_list.json'


def download():
    # For a list of audio need to download
    audio_list = get_audio_list_from_file(AUDIO_LIST_INPUT_FILE, sort=True)

    # Download audio list
    download_audios(audio_list)


def download_audios(audio_list):
    for item in audio_list:
        fn = ''.join(['data/', str(item['id']), '.txt'])
        file = open(fn, 'w')

        for audio in item['audios']:
            # Extract filename
            audio_name = get_filename_from_url(audio['audio_url'])
            audio_path = 'data/%s' % audio_name
            # Download from S3
            get = get_remote_audio(audio, audio_path)
            if not get:
                print('Error while downloading {}'.format(audio_name))
            else:
                print('{} downloaded successfully!'.format(audio_name))
            # Write filename to files list
            file.write("file 'data/{}'\n".format(audio_name))

        file.close()

if __name__ == '__main__':
    download()
