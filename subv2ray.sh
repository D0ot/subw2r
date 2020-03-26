#/bin/bash

echo "Simple Script for V2ray Subscription START"

export temp=$(mktemp)

wget -O- $(cat url.txt) > ${temp}

echo '==' >> ${temp}

base64 -d -i < ${temp} | python ./vmess2json/vmess2json.py --parse_all

rm ${temp}

python test_servers.py

echo "Simple Script for V2ray Subscription END"