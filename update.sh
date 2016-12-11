#!/bin/sh
./plot.py
git add . -A
git commit -m "update"
git push
