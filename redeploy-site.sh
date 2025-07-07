#!/usr/bin/bash

echo $'\nKilling active tmux server \n'
$(tmux kill-server)

echo $'\n Fetching changes from remote repository\n'
$(git -C ~/portfolio-site fetch)
RESULT=$(git -C ~/portfolio-site reset origin/main --hard)
echo $0
echo "$RESULT"

PIP=$(source ./python3-virtualenv/bin/activate && pip install -r ~/portfolio-site/requirements.txt)
echo"$PIP"
$(tmux new -d -s portfolio)

$(tmux send -t portfolio.0 'cd ~/portfolio-site' ENTER)

$(tmux send -t portfolio.0 'source ~/portfolio-site/python3-virtualenv/bin/activate' ENTER)

$(tmux send -t portfolio.0 'export FLASK_ENV=development' ENTER)

$(tmux send -t portfolio.0 'flask run --host=0.0.0.0' ENTER)
