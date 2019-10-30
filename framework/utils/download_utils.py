import requests

from framework.utils.logger import info


def download_file(url, path):
    info(f"Downloading file from {url} and saving in {path}")
    with open(path, "wb") as download_file:
        download_file.write(requests.get(url).content)
