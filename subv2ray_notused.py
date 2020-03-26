from urllib.request import urlopen
from base64 import b64decode
from vmess2json.vmess2json import parseVmess
import sh


def read_file(fn : str):
    f = open(fn, 'r')
    content = f.read()
    f.close()
    return content

def get_vmess_from_subsciption(code : str):
    share_links = b64decode(code + '==').decode('utf-8')
    return share_links

def get_vmess_from_subscription_url(subscripe_url : str):
    return_content = urlopen(subscripe_url, timeout=3).read().decode('utf-8')
    return get_vmess_from_subsciption(return_content)


if __name__ == "__main__":
    filename = 'url.txt'
    url = read_file(filename)
    vmess_str = get_vmess_from_subscription_url(url)
    print(vmess_str)
    sh.env('./vmess2json/vmess2json.py', '-parse_all')

