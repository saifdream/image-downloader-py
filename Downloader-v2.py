import os
import json
import urllib.request
from threading import Thread
from urllib.error import URLError


class Downloaderv2(Thread):
    def __init__(self, url):
        super().__init__()
        self.killed = False
        self.url = url

    def run(self):
        try:
            print("Thread started ...")
            urllib.request.urlretrieve(self.url, "fixit-img-v2-v1/" + self.url.split('/')[-1])
            print("Thread finished!")
        except:
            # print(e)
            f = open("error-v1.1.txt", "a")
            f.write(self.url)
            f.write("\n")
            f.close()
        print("Done")
        # raise SystemExit()


def main():
    image_url_list = set()
    if os.path.isfile("fixit.json"):
        with open('fixit.json') as json_file:
            data = json.load(json_file)
            for u in data:
                image_url_list.add(u)

    for url in image_url_list:
        if not os.path.isfile("fixit-img-v2-v1/" + url.split('/')[-1]):
            Downloaderv2(url).start()


if __name__ == '__main__':
    main()
