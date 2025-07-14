#!/usr/bin/bash
echo $'\nFetching changes from remote repository\n'

FETCH=$(cd ~/portfolio-site && git fetch && git reset origin/main --hard)
echo "$FETCH"

echo $'\n\nInstalling dependencies\n'
PIP=$(source ./python3-virtualenv/bin/activate && pip install -r ~/portfolio-site/requirements.txt)

echo "$PIP"


echo $'\nReloading daemon\n'
$(systemctl daemon-reload)

echo $'\nRestarting service\n'
$(systemctl restart myportfolio)

