#!/bin/bash
set -e

cp ../Fitxbot /opt/Fitxbot
cp fitxbot.service /lib/systemd/system/
chmod +x /opt/Fitxbot/run_bot.sh
systemctl enable fitxbot.service