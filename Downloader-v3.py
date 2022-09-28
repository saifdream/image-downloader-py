import os
from threading import Thread
from urllib.parse import quote_plus


class Downloaderv3(Thread):
    def __init__(self, url, file_name):
        super().__init__()
        self.killed = False
        self.url = url
        self.file_name = file_name

    def run(self):
        try:
            print("Thread started ...")
            import urllib.request
            urllib.request.urlretrieve(self.url, "machineandtoolsbd-img/" + self.file_name)
            print("Thread finished!")
        except:
            # print(e)
            f = open("machineandtoolsbd-error.txt", "a")
            f.write(self.url)
            f.write("\n")
            f.close()
        print("Done")
        # raise SystemExit()


def image_name_beautifier(image_name):
    print("image name: [" + image_name + "]")
    # return image_name.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
    return image_name.translate({ord(c): " " for c in "'\","})


def main():
    if os.path.isfile("machineandtoolsbd.txt"):
        with open('machineandtoolsbd.txt') as f:
            for url in f:
                stripped_url = url.strip()
                original_image_name = stripped_url.split('/')[-1]
                img_file = image_name_beautifier(original_image_name)
                encoded_image_name = quote_plus(original_image_name)
                if not os.path.isfile("machineandtoolsbd-img/" + img_file):
                    modified_url = stripped_url.replace(original_image_name, encoded_image_name)
                    print("Modified image name: [" + img_file + "]")
                    print("Encoded image name: [" + encoded_image_name + "]")
                    print("modified url: [" + modified_url + "]")
                    Downloaderv3(modified_url, img_file).start()


if __name__ == '__main__':
    main()
