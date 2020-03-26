#!/bin/bash

sudo echo "Simple Script for V2ray Subscription START"

export temp=$(mktemp)

wget -O- $(cat url.txt) > ${temp}

echo '==' >> ${temp}

base64 -d -i < ${temp} | python ./vmess2json/vmess2json.py --parse_all

rm ${temp}

python test_servers.py

sudo mkdir -p /etc/v2ray/jiyou

sudo cp *.json /etc/v2ray/jiyou

rm *.json

echo "Simple Script for V2ray Subscription END"