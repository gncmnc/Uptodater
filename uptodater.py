# -*- coding: utf-8 -*-


"""
Who Contributed
gncmnc <https://github.com/gncmnc>
Samet195 <https://github.com/Samet195>
CihatAltiparmak <http://github.com/CihatAltiparmak>
"""

import requests, socket
from requests.exceptions import ConnectionError
from requests.exceptions import InvalidURL
from colorama import Fore, init

init(autoreset=True)

class Uptodater():
    def github_informations(github_link, version, version_file):
        print(Fore.LIGHTGREEN_EX  + "GitHub address : " + github_link)
        print(Fore.LIGHTGREEN_EX + "This version : " + version)
        print(Fore.LIGHTGREEN_EX + "Version file to search : " + version_file)

    def connect(version, version_file):
        try:
            pass

        except InvalidURL:
            pass

        except ConnectionError:
            pass
        
        def compare(version, version_file):
            pass

    def uptodate():
        pass
