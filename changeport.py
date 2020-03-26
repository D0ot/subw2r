import os
import json

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
        new_file_name = str(index) + '.json'
        os.rename(fn, new_file_name)
        index = index + 1
        json_file = json.loads(read_file(new_file_name))
        for inbound in json_file['inbounds']:
            # change the port number
            if inbound['tag'] == 'socks-in':
                inbound['port'] = 10801
            if inbound['tag'] == 'http-in':
                inbound['port'] = 8124
        new_json_file_content = json.dumps(json_file, indent=4)
        rewrite_file(new_file_name, new_json_file_content)


    