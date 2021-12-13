#!/usr/bin/env python3

import yaml

if __name__ == '__main__':
    with open('clash-source.yml', 'r', encoding='utf-8') as f:
        txt = f.read()
        yml = yaml.safe_load(txt)

    proxies = ['DIRECT'] + [p['name'] for p in yml['proxies']] + ['REJECT']
    for group in yml['proxy-groups']:
        if 'type' not in group:
            group['type'] = 'select'
        group['proxies'] = proxies

    with open('../clash.yml', 'w', encoding='utf-8') as f:
        f.write(yaml.safe_dump(yml, allow_unicode=True))
