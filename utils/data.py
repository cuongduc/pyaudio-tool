"""
Some utilities for data
"""
import json
import urllib.request

from operator import itemgetter


def get_audio_list_from_file(filename, sort=True):
    f = open(filename, 'r')
    raw = f.read()
    audio_list = json.loads(raw)

    if sort:
        audio_list = sort_audio_list(audio_list)

    return audio_list


def sort_audio_list(audio_list):
    """
    Sort the audios array in each audio item
    by audioable_id
    """
    for item in audio_list:
        if 'audios' not in item:
            raise KeyError('Invalid audio list!')
        audios = item['audios']
        sorted_audios = sorted(
            audios, key=itemgetter('audioable_id', 'audio_url'))
        item['audios'] = sorted_audios

    return audio_list


def get_remote_audio(audio, output_name):
    url = audio['audio_url']
    get = urllib.request.urlretrieve(url, output_name)

    if not get:
        return False

    return True
