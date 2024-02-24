# -*- coding: utf-8 -*-
# BY: TONG

import argparse
import requests

url='http://10.0.0.55:801/include/auth_action.php'

def login(u, p):
    postdata=dict([('ac_id', 1), ('save_me', 1), ('ajax', 1)])
    postdata['username']=u
    postdata['password']=p
    postdata['action']='login'

    r=requests.post(url, postdata)
    r.encoding='utf-8'

    if r.text.split(',')[0] == 'login_ok':
        print(":)")
    else:
        print(":(")
    
    #print(r.text)

def logout(u, p):
    postdata=dict([('ajax', 1)])
    postdata['username']=u
    postdata['password']=p
    postdata['action']='logout'

    r=requests.post(url, postdata)

    #default encoding is ISO-8859-1
    r.encoding='utf-8'
    print(r.text)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get your campus network without a desktop environment')

    parser.add_argument('-u', type=str, required=True, metavar='USERNAME', help="username (required)")
    parser.add_argument('-p', type=str, required=True, metavar='PASSWORD', help="password (required)")
    parser.add_argument('-a',   type=str, required=True, metavar='ACTION', help="action:login|logout (required)")

    args = parser.parse_args()

    if args.a == 'login':
        login(args.u, args.p)
    elif args.a == 'logout':
        logout(args.u, args.p)
    else:
        raise ValueError('Unknown action: {:s} (login|logout)'.format(args.a))
