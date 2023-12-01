import requests
import os
from bs4 import BeautifulSoup
url = 'https://xkcd.com/1/'
if not os.path.exists('xkcd_comics'):
    os.makedirs('xkcd_comics')
comic_number = 1
while True:
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        comic_elem = soup.select('#comic img')

        if not comic_elem:
            print(f'Could not find comic image for {url}')
        else:
            comic_url = 'https:' + comic_elem[0].get('src')
            file_name = os.path.basename(comic_url)
            file_path = os.path.join('xkcd_comics', file_name)

            if not os.path.isfile(file_path):
                print(f'Downloading {comic_url}...')
                res = requests.get(comic_url)
                res.raise_for_status()

                with open(file_path, 'wb') as image_file:
                    for chunk in res.iter_content(100000):
                        image_file.write(chunk)
                print(f'Saved {file_name}')
            else:
                print(f'Skipped {file_name} (already exists)')
        prev_link = soup.select('a[rel="prev"]')[0]

        if not prev_link:
            print('No more comics to download.')
            break
        url = 'https://xkcd.com' + prev_link.get('href')
        comic_number += 1
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        break
print(f'Downloaded {comic_number} comics in total.')