#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
echo $SCRIPT_DIR

sudo apt intstall python3

cd /opt
sudo git clone https://github.com/yn4k4nishi/git-prefix-tool.git

sudo chmod 777 git-prefix-tool/git-prefix-tool.sh

sudo ln git-prefix-tool/git-prefix-tool.sh /usr/local/bin/git-prefix-tool

cd $SCRIPT_DIR