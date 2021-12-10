#!/bin/bash
WorkPath='/root/CSU_China_Union_autoLogin/'
cd $WorkPath
logDir=`date +"+%Y-%m-%d"`
if [ -e $logDir ]
then
    :
else
    mkdir $logDir
fi
python3 -u ./autoLogin.py &>>./$logDir/log_`date +%H`.txt