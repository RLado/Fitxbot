# Fitxbot
## Auto clock in/out bot for IQS Cezzane

This bot is intended to be run on a raspberry pi or any other linux system. To do so you have to configure your clock in/out times on the configuration .ini file and provide your username and password. Once the configuration has been written modify run_bot.sh to point to your configuration file and run the install.sh script.

Alternatively if you want to run the bot only once you can:
```bash
python3 python3 autofb.py -c <your config>.ini > /var/log/fitxbot_<your name>.log
```

### Setup
In order to run this bot firefox and geckodriver must be on your system. Once you have firefox installed you can download the geckodriver from here: https://github.com/mozilla/geckodriver/releases

Put the geckodriver binary on the main Fitxbot folder and then run the bot either by using install.sh and rebooting, or using it as a simple pyhton script.