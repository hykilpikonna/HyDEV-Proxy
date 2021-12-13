#!/usr/bin/env python3

import ruamel.yaml

if __name__ == '__main__':
    yaml = ruamel.yaml.YAML()

    with open('clash-source.yml', 'r', encoding='utf-8') as f:
        yml = yaml.load(f)

    proxies = ['DIRECT'] + [p['name'] for p in yml['proxies']] + ['REJECT']
    for group in yml['proxy-groups']:
        if 'type' not in group:
            group['type'] = 'select'
        group['proxies'] = proxies

    with open('../clash.yml', 'w', encoding='utf-8') as f:
        yaml.dump(yml, f)
