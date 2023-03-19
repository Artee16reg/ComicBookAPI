import requests
import hashlib
import datetime


timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
pub_key = '84ee796520f165c94489aceffd687bb1'
priv_key = '16cc27910f450fa73a3b2b552c617f4bccc7710d'


def hash_params():
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params


params = {
    'ts': timestamp,
    'apikey': pub_key,
    'hash': hash_params(),
    'limit': 5
}


def comics_list(request):
    if request.GET.get('titleStartsWith'):
        params['titleStartsWith'] = request.GET.get('titleStartsWith')
    result = requests.get(f'https://gateway.marvel.com:443/v1/public/comics',
                          params=params)

    return result.json()


def comic_detail(pk):
    """
    Парсер получение название, описание, дата выхода, все связанные картинки,
    список персонажей в выпуске и stories
    """

    result = requests.get(f'https://gateway.marvel.com:443/v1/public/comics/{pk}',
                          params=params)
    images_url = ''
    if result.json()['data']['results'][0]['images']:
        '''путь картинки'''
        images_url = result.json()['data']['results'][0]['images'][0]['path']
        images_url = images_url + '.' + result.json()['data']['results'][0]['images'][0]['extension']

    comic_book_detail = {
        'title': result.json()['data']['results'][0]['title'],
        'description': result.json()['data']['results'][0]['description'],
        'modified': result.json()['data']['results'][0]['modified'],
        'images': images_url,
        # 'characters': result.json()['data']['results'][0]['characters'],
        # 'stories': result.json()['data']['results'][0]['stories'],
    }

    return comic_book_detail
