import requests
from bs4 import BeautifulSoup

def parse_artist(id_):
    r = requests.get('https://mp3push.com/hits-music/')
    soup = BeautifulSoup(r.text, 'lxml')
    artists = soup.find_all("span", class_ = 'title_artist')
    return artists

def parse_songs(id_):
    r = requests.get('https://mp3push.com/hits-music/')
    soup = BeautifulSoup(r.text, 'lxml')
    songs = soup.find_all("li", class_ = 'item-wrap')
    return songs

def parse_songs_names(id_):
    r = requests.get('https://mp3push.com/hits-music/')
    soup = BeautifulSoup(r.text, 'lxml')
    song_names = soup.find_all("span", class_ = 'song-title')
    return song_names

def parse_name(id_):
    r = requests.get('https://mp3push.com/hits-music/')
    soup = BeautifulSoup(r.text, 'lxml')
    title_audio = soup.find_all("a", class_ = 'title_audio')
    return title_audio

def parse_photo(id_):
    r = requests.get(f'https://mp3push.com{parse_name(id_)[int(id_)-1].attrs["href"]}', headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'})
    print(r.headers)
    soup = BeautifulSoup(r.text, 'lxml')
    photo = soup.find_all('img')
    return photo