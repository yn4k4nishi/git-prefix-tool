#! /usr/bin/python3
# -*- coding: utf-8 -*-

import yaml

def main():
    # 設定ファイルの読み込み
    with open('config.yml','r') as yml:
        config = yaml.load(yml, Loader=yaml.SafeLoader)

    for p in config['prefix']:
        print('> ' + p)


if __name__ == "__main__":
    main()