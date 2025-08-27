#!/bin/bash

cd /home/ml150914/Desktop/AirPi_tst1/air-quality-project
cp /home/ml150914/Desktop/AirPi_tst1/$(date +%F).csv .

git add *.csv
git commit -m 'Update log $(date +%F)'
git push
