#!/bin/bash

tmux kill-server
cd /root/portfolio-site
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new -d 'cd /root/portfolio-site; flask run --host=0.0.0.0'
