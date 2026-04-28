#!/bin/bash
git init
dvc init
echo "data/raw/" >> .gitignore
echo "data/processed/" >> .gitignore
echo "models/" >> .gitignore
echo "__pycache__/" >> .gitignore
git add .gitignore .dvc/config
git commit -m "Initialize DVC and Git"