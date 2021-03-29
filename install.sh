#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

cd /opt
sudo git clone https://github.com/yn4k4nishi/git-prefix-tool.git

sudo chmod 777 git-prefix-tool/git-prefix-tool.sh
sudo chmod 777 git-prefix-tool/python/*.py

sudo ln /opt/git-prefix-tool/git-prefix-tool.sh /usr/local/bin/git-prefix-tool

cd $SCRIPT_DIR