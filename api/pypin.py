
from api.downloader import download
from api.tools import *
TYPES = [
    'Video',
    'GIF',
    'Image',
]


def downloadPinterestMedia(url):
    NAME, HTML = getHtml(url)
    if NAME == None:
        print('[ERROR] Not a Valid Pinterest URL')

    JSON = getJson(HTML)
    TYPE, MEDIA_URL = decideType(JSON)

    if TYPE == None:
        print('[404] Nothing Found!')

    file_name = f'{NAME}.{MEDIA_URL.split(".")[-1]}'

    print(f'Downloading {TYPES[TYPE]}: {file_name}')
    download(MEDIA_URL, file_name)
    return file_name
