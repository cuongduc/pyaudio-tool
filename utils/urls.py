"""
Some utilities for processing url
"""


def get_filename_from_url(url):
    return url.split('/')[-1:][0]


def generate_upload_filename(url):
    segment_name = get_filename_from_url(url)
    file_name = segment_name.split('_')[:2]
    file_name = '_'.join(file_name)
    upload_filename = ''.join([file_name, '.mp3'])

    return upload_filename
