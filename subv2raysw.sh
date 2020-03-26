#!/bin/bash

V2RAY_CONFIG_FILE="/etc/v2ray/config.json"

index=$1

filename="/etc/v2ray/jiyou/${index}.json"

sudo systemctl stop v2ray.service

sudo mv ${filename} ${V2RAY_CONFIG_FILE}

sudo systemctl start v2ray.service


