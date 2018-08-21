import os
import platform
import requests
import zipfile


class WebDriverUpdate:
    INSTALLED_RELEASE_FILE = "INSTALLED_RELEASE"
    LATEST_RELEASE_FILE = "LATEST_RELEASE"
    WEBDRIVER_URL = "https://chromedriver.storage.googleapis.com"

    def __init__(self):
        self._create_installed_release_file()
        self._installed_release = self._get_installed_release()
        self._latest_release = self._get_latest_release()

    def has_update(self):
        return self._installed_release != self._latest_release

    def latest_release(self):
        return self._latest_release

    def installed_release(self):
        return self._installed_release

    def update(self):
        filename = self._get_os_webdriver_filename()
        source = "{}/{}/{}".format(WebDriverUpdate.WEBDRIVER_URL, self._latest_release, filename)
        self._download_file(source)
        self._unzip_and_remove(filename)
        self._update_installed_release_file(self._latest_release)

    def _get_os_webdriver_filename(self):
        os_mapped_filename = {
                "linux": "chromedriver_linux64.zip",
                "macos": "chromedriver_mac64.zip",
                "windows": "chromedriver_win32.zip",
        }

        os = platform.system().lower()
        return os_mapped_filename[os]

    def _create_installed_release_file(self):
        if not os.path.exists(WebDriverUpdate.INSTALLED_RELEASE_FILE):
            with open(WebDriverUpdate.INSTALLED_RELEASE_FILE, "w") as f:
                f.write("0.0")
            f.close()

    def _get_installed_release(self):
        with open(WebDriverUpdate.INSTALLED_RELEASE_FILE, "r") as f:
            version = f.read()
        f.close
        return float(version)

    def _get_latest_release(self):
        self._download_latest_release_file()
        with open(WebDriverUpdate.LATEST_RELEASE_FILE, "r") as f:
            version = f.read()
        f.close
        return float(version)

    def _download_latest_release_file(self):
        r = requests.get(WebDriverUpdate.WEBDRIVER_URL + "/" + WebDriverUpdate.LATEST_RELEASE_FILE)
        with open(WebDriverUpdate.LATEST_RELEASE_FILE, "wb") as f:
            f.write(r.content)
        f.close()

    def _download_file(self, url):
        local_filename = url.split('/')[-1]
        r = requests.get(url)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        f.close()

    def _unzip_and_remove(self, filename):
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(".")
        os.remove(filename)

    def _update_installed_release_file(self, release):
        with open(WebDriverUpdate.INSTALLED_RELEASE_FILE, "w") as f:
            f.write(str(release))
        f.close()
        self._installed_release = self._get_installed_release()
