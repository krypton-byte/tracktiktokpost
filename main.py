from requests import Session
from json import (
    loads,
    dumps
)
from re import findall
from os.path import exists
from argparse import ArgumentParser


class Post(Session):

    def __init__(self, username: str, comparisonfile: str) -> None:
        super().__init__()
        self.headers:dict = {'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': 'Linux', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'origin': 'https://tiktok.com', 'referer': 'https://tiktok.com', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36', 'X-Forwarded-For': '196.136.217.211'}
        self.username = findall(r'@([a-zA-Z0-9\_]+)', username)[0] if '@' in username else username
        self.comparison = loads(open(comparisonfile, 'r').read()) if exists(comparisonfile) else []
        self.comparisonfile = comparisonfile

    def lpost(self):
        userpage = self.get(f'https://www.tiktok.com/@{self.username}').text
        all_post = findall(r'href=\"(https?://www.tiktok.com/@[A-Za-z0-9_]+/video/[0-9]+)\"', userpage)
        newpost = set(all_post) - set(self.comparison)
        open('index.html', 'w').write(userpage)
        if newpost:
            print(f'Latest Post: {list(newpost)}')
            self.comparison.extend(list(newpost))
            open(self.comparisonfile, 'w').write(dumps(self.comparison, indent=4))
        else:
            print('No recent post')


arguments = ArgumentParser()
arguments.add_argument('--username', type=str, required=True)
arguments.add_argument('--file', type=str, required=True)
parse = arguments.parse_args()
Post(parse.username, parse.file).lpost()