# -*- coding: utf-8 -*-
"""
main.py

Created by <jimokanghanchao@gmail.com> on Dec 04,2015
"""

def main():
  import argparse
  parser = argparse.ArgumentParser(description="初始化APIClient对象")
  parser.add_argument("-key", "--key", type=str,\
    help="input the APP_KEY", default="4123398440")
  parser.add_argument("-secret", "--secret", type=str,\
    help="input the APP_SECRET", default="104ece76059afa20bca62aa5d9554704")
  parser.add_argument("-url", "--url", type=str,\
    help="input the CALLBACK_URL", default="http://127.0.0.1/callback")
  parser.add_argument("-token", "--token", type=str,\
    help="input the ACCESS_TOKEN", default="2.00hYRkpC9S3DVE203bceb0140FaZub")
  group_authcode_token = parser.add_mutually_exclusive_group(required=False)
  group_authcode_token.add_argument("-request_authcode", "--request_authcode", type=bool,\
    help="whether make a request to access CALLBACK_URL to get the code, True or False?", default=False)
  group_authcode_token.add_argument("-request_token", "--request_token", type=bool,\
    help="whether make a request to get the new ACCESS_TOKEN, True or False?", default=False)
  parser.add_argument("-code", "--code", type=str,\
    help="code used to get the new ACCESS_TOKEN")
  parser.print_help()
  args = parser.parse_args()
  #print args

  APP_KEY = args.key
  APP_SECRET = args.secret 
  CALLBACK_URL = args.url
  ACCESS_TOKEN = args.token

  from snspy import APIClient,SinaWeiboMixin
  if args.request_authcode:
    client = APIClient(SinaWeiboMixin,app_key=APP_KEY,app_secret=APP_SECRET,redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    print "the authorize url: %s used to get the authcode" % url
  elif args.request_token and args.code:
    client = APIClient(SinaWeiboMixin,app_key=APP_KEY,app_secret=APP_SECRET,redirect_uri=CALLBACK_URL)
    r = client.request_access_token(args.code)
    print "the new access token:%s" % r
  else:
    client = APIClient(SinaWeiboMixin,app_key=APP_KEY,app_secret=APP_SECRET,redirect_uri=CALLBACK_URL,access_token=ACCESS_TOKEN)
    print client._mixin.__dict__
    print client.statuses.mentions.get()

if __name__ == '__main__':
  main()
