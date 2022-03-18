import os
import urllib.request
import zipfile
from _socket import timeout
from http.client import IncompleteRead
from io import BytesIO
from urllib.parse import urlparse
import _socket

_socket.setdefaulttimeout(10)  # set timeout


def ransomware_and_malware_domain_check(list_of_domains):
    while True:
        try:
            list_of = urllib.request.urlopen(
                "https://raw.githubusercontent.com/blocklistproject/Lists/master/ransomware.txt").read().decode(
                errors='replace').strip().split("\n")
        except IncompleteRead:
            continue
        except timeout:
            list_of = ""
            break
        break

    list_of_mal_domains = []

    for n in list_of:
        if n and not n.startswith("#"):
            list_of_mal_domains.append(n.strip())

    while True:
        try:
            list_of = urllib.request.urlopen(
                "https://raw.githubusercontent.com/blocklistproject/Lists/master/malware.txt").read().decode(
                errors='replace').strip().split("\n")
        except IncompleteRead:
            continue
        except timeout:
            list_of = ""
            break
        break

    list_of_mal_urls = []

    for n in list_of:
        if n and not n.startswith("#"):
            n = n.replace("0.0.0.0 ","")
            n = urlparse(n).netloc
            if n.startswith("www."):
                n = ".".join(n.split(".")[1:])
            list_of_mal_urls.append(n)

    list_of = set(list_of_mal_domains + list_of_mal_urls)

    mal_in_my_domains = []
    for mal_dom in list_of:
        for i, my_dom in enumerate(list_of_domains):
            if mal_dom in my_dom:
                mal_in_my_domains.append(mal_dom)
                list_of_domains[i] = mal_dom




    urllib.request.urlopen("https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware")
#    with zipfile.ZipFile(BytesIO(urlfile.read())) as z:
#        z.extract("justdomains")
    my_malware_domains = []
    malware_domains = []
#    with open("justdomains", 'r') as malware_domains:
    #list_of_malware_domains = malware_domains.readlines()
    for mal_dom in malware_domains:
        mal_dom = mal_dom.strip()
        if mal_dom:
            if mal_dom.startswith("www."):
                mal_dom = ".".join(mal_dom.split(".")[1:])
            for i, my_domain in enumerate(list_of_domains):
                if mal_dom in my_domain:
                    my_malware_domains.append(mal_dom)
                    list_of_domains[i] = mal_dom
    #os.remove("justdomains")
    mal_in_my_domains = set(mal_in_my_domains)
    my_malware_domains = set(my_malware_domains)
    normal_domains = set(list_of_domains) - mal_in_my_domains - my_malware_domains

    return normal_domains, mal_in_my_domains, my_malware_domains
