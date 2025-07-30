#!/bin/bash

git config --global user.name "Ilya Vostrikov"
git config --global user.email "ilyavostrikov90@gmail.com"   # ← свой GitHub email

git init  # если не инициализирован
git add .
git commit -m "First commit 🚀"

git remote remove origin 2> /dev/null
git remote add origin https://github.com/IlyaVostrikov/telegram-webapp-ne-stidno.git

git branch -M main
git push -u origin main
