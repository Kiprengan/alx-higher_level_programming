#!/bin/bash
read -p "Enter the git add argument: " add_argument
read -p "Enter the git commit message: " commit_message

git add "$add_argument"
git commit -m "$commit_message"
git push
