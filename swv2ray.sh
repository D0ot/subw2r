#!/bin/bash

V2RAY_CONFIG_FILE="/etc/v2ray/config.json"

filename=$1

sudo systemctl stop v2ray.service

sudo cp ${filename} ${V2RAY_CONFIG_FILE}

sudo systemctl start v2ray.service


