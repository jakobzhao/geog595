#!/bin/sh
python env_sensor.py
cd ../repo_local_path
git checkout -f
git fetch
git pull
git commit -i "update"
git push
