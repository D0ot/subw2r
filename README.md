# Simple Script for v2ray subscription

---

## How to use

after git clone you should

```sh
git submodule update --init
```

1. add subscription url in `url.txt`
2. `./subv2ray.sh` to get subscriptions in ./tmp folder
3. `./swv2ray.sh tmp/{something}.json` to switch server we use

## Default Config

socks5: localhost:10801

http:localhost:10802
