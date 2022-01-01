#!/usr/bin/bash
git config user.name "github-actions"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git add .
git commit -m 'update'
if [ $? = 1 ]; then
    echo "No recent Post"
else
    git push
fi