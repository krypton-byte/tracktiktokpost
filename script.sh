#!/usr/bin/bash

git config user.name "github-actions"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com""
git add .
git commit -m 'update'
if [[ $? == 1 ]]; then
    git push
else
    echo "No recent Post"
fi