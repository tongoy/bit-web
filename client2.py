# -*- coding: utf-8 -*-
# BY: TONG

"""
BIT web script.
"""

import os
import time
import json
import requests
import argparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

# url='http://10.0.0.55/srun_portal_pc?ac_id=1&theme=bit'
url='http://10.0.0.55'


# The script uses selenium+chromedriver to login the system, and print the status information.
def login(u, p):
    try:
        # driver.find_element_by_id("username").send_keys(u)
        driver.find_element(By.ID, "username").send_keys(u)
        # driver.find_element_by_id("password").send_keys(p)
        driver.find_element(By.ID, "password").send_keys(p)
        # login_btn = driver.find_element_by_id("login")
        login_btn = driver.find_element(By.ID, "login")
        login_btn.click()
        time.sleep(5)
        
        # get status about login
        browser_log_list = driver.get_log("performance")

        status_url = None
        status_dict = None
        for log in browser_log_list:
            message = json.loads(log['message'])['message']
            if 'method' in message and message['method'] == 'Network.requestWillBeSent':
                if 'params' in message and 'request' in message['params'] and 'url' in message['params']['request']:
                    request_url = message['params']['request']['url']
                    if request_url.startswith("http://10.0.0.55/cgi-bin/srun_portal?callback"):
                        status_url = request_url
                        # print(status_url)
                        break
        
        r = requests.get(status_url)
        if r.status_code == requests.codes.ok:
            status_dict = json.loads(r.text[r.text.find('(')+1: r.text.find(')')])
            # print(status_dict)
            print("{:s}, ip={:s}".format(status_dict['error'], status_dict['client_ip']))
            if status_dict['error_msg']: print(status_dict['error_msg'])
        else:
            print("login status unknown")

        # logs = [json.loads(log['message'])['message'] for log in browser_log_list]
        # with open('./log.json', 'w') as f:
        #     json.dump(logs, f, indent=4, ensure_ascii=False)

    
    except (ElementNotInteractableException, NoSuchElementException):
        print("ip_already_online_error")



def logout(u, p):
    try:
        # logout_btn = driver.find_element_by_id("logout")
        logout_btn = driver.find_element(By.ID, "logout")
        logout_btn.click()
        time.sleep(5)
    except NoSuchElementException:
        print("ip_not_online_error")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get your campus network without a desktop environment')
    parser.add_argument('-u', type=str, required=True, metavar='USERNAME', help="username (required)")
    parser.add_argument('-p', type=str, required=True, metavar='PASSWORD', help="password (required)")
    parser.add_argument('-a', type=str, required=True, metavar='ACTION', help="action:login|logout (required)")
    args = parser.parse_args()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # TypeError: WebDriver.__init__() got an unexpected keyword argument 'desired_capabilities'.
    # caps = DesiredCapabilities.CHROME
    # caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    # driver = webdriver.Chrome(desired_capabilities=caps, options=chrome_options)
        
    chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    # print(driver.current_url)
    time.sleep(5)

    if args.a == 'login':
        login(args.u, args.p)
    elif args.a == 'logout':
        logout(args.u, args.p)
    else:
        raise ValueError('Unknown action: {:s} (login|logout)'.format(args.a))

    
    driver.quit()
