import os
import sh


if __name__ == "__main__":

    file_list = os.listdir('.')
    json_files = []
    for fn in file_list:
        if fn.endswith('.json'):
            json_files.append(fn)
    
    index = 0
    for fn in json_files:
        os.rename(fn, str(index) + '.json')
        index = index + 1

    # change the port number

    with sh.contrib.sudo:
        sh.systemctl.stop('v2ray.service')