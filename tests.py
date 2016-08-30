from utils.urls import generate_upload_filename
from utils.data import get_audio_list_from_file
from utils.helpers import var_dump


def test_get_audio_list_from_file():
    data_file = 'data/audio_list.json'
    audio_list = get_audio_list_from_file(data_file, sort=True)
    var_dump(audio_list)


def test_generate_upload_filename():
    url = 'https://s3-ap-northeast-1.amazonaws.com/testaudiodemo/uploads/audios/23_How-to-make-a-tough-dad-cry--His-son-making-the-Olympic-boxing-team_129.mp3'
    file_name = generate_upload_filename(url)
    var_dump(file_name)

if __name__ == '__main__':
    # test_generate_upload_filename()
    test_get_audio_list_from_file()
