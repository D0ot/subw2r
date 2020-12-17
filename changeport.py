# -*- coding: UTF-8 -*-    

import os
import json

# 设置你需要的本地代理端口
socks_port = 10801
http_port = 10802


def read_file(fn : str):
    f = open(fn, 'r')
    content = f.read()
    f.close()
    return content

def rewrite_file(fn : str, content : str):
    f = open(fn, 'w')
    f.write(content)
    f.close()

if __name__ == "__main__":

    file_list = os.listdir('.')
    json_files = []
    for fn in file_list:
        if fn.endswith('.json'):
            json_files.append(fn)
    
    index = 0
    for fn in json_files:
        index = index + 1
        json_file = json.loads(read_file(fn))
        for inbound in json_file['inbounds']:
            # change the port number
            if inbound['tag'] == 'socks-in':
                inbound['port'] = socks_port
            if inbound['tag'] == 'http-in':
                inbound['port'] = http_port
        new_json_file_content = json.dumps(json_file, indent=4)
        rewrite_file(fn, new_json_file_content)


    
