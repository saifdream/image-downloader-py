import os
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from urllib.error import URLError
from urllib.parse import quote_plus


def image_name_beautifier(image_name):
    print("image name: [" + image_name + "]")
    return image_name.translate({ord(c): " " for c in "'\","})


def downloader(url):
    import urllib.request
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/74.0.3729.131 Chrome/74.0.3729.131 Safari/537.36')]
    urllib.request.install_opener(opener)

    try:
        original_image_name = url.split('/')[-1]
        img_file = image_name_beautifier(original_image_name)
        encoded_image_name = quote_plus(original_image_name)
        modified_url = url.replace(original_image_name, encoded_image_name)

        print("Thread started ...")
        if not os.path.isfile("img/" + img_file):
            urllib.request.urlretrieve(modified_url, "img/" + img_file,
                                       )
        print("Thread finished!")
    except URLError as e:
        print(e)
        f = open("error.txt", "a")
        f.write(url)
        f.write("\n")
        f.close()
    print("Done")


def main():
    image_url_list = set()
    if os.path.isfile("bearing.txt"):
        with open('bearing.txt') as f:
            for url in f:
                stripped_url = url.strip()
                image_url_list.add(stripped_url)

    print("Starting ThreadPoolExecutor")
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(downloader, image_url_list)
    print("All tasks complete")


if __name__ == '__main__':
    main()
