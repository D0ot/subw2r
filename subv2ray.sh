#!/bin/bash

sudo echo "Simple Script for V2ray Subscription START"

export temp=$(mktemp)

wget -O- $(cat url.txt) > ${temp}

echo '==' >> ${temp}

base64 -d -i < ${temp} | python ./vmess2json/vmess2json.py --parse_all

rm ${temp}

python changeport.py

mkdir -p ./tmp

mv *.json ./tmp

echo "Simple Script for V2ray Subscription END"
