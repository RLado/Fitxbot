import schedule
import time
import configparser
import argparse
import os

import webbot


if __name__=='__main__':
    #Argument parser
    parser=argparse.ArgumentParser(description='Run the clock in/out bot')
    parser._action_groups.pop()
    required=parser.add_argument_group('required arguments')
    optional=parser.add_argument_group('optional arguments')

    required.add_argument('-c','--config',type=str,help='Config file containing username and password',required=True)
    args=parser.parse_args()

    #Read config file
    config=configparser.ConfigParser()
    if os.path.isfile(args.config):
        config.read(args.config)
    else:
        raise FileNotFoundError('Could not load the configuration file.')

    def ci():
        webbot.clock_in(config['Login']['USER'],config['Login']['PASSWD'])
    def co():
        webbot.clock_out(config['Login']['USER'],config['Login']['PASSWD'])

    #Schedule clock in and out tasks for every day
    schedule.every().monday.at(config['Schedule']['MON_IN']).do(ci)
    schedule.every().monday.at(config['Schedule']['MON_OUT']).do(co)

    schedule.every().tuesday.at(config['Schedule']['TUE_IN']).do(ci)
    schedule.every().tuesday.at(config['Schedule']['TUE_OUT']).do(co)

    schedule.every().wednesday.at(config['Schedule']['WED_IN']).do(ci)
    schedule.every().wednesday.at(config['Schedule']['WED_OUT']).do(co)

    schedule.every().thursday.at(config['Schedule']['THU_IN']).do(ci)
    schedule.every().thursday.at(config['Schedule']['THU_OUT']).do(co)

    schedule.every().friday.at(config['Schedule']['FRI_IN']).do(ci)
    schedule.every().friday.at(config['Schedule']['FRI_OUT']).do(co)

    #Keep script alive
    while True: 
        # Checks whether a scheduled task is pending to run or not 
        schedule.run_pending() 
        time.sleep(1) 